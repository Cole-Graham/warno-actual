"""Configuration loading and validation."""

import logging
from copy import deepcopy
from pathlib import Path

import ruamel.yaml

logger = logging.getLogger(__name__)

_DEVELOPER_CONFIG_NAMES = {"config.yaml", "config.yml"}


def _round_trip_yaml() -> ruamel.yaml.YAML:
    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096
    # Match the template: nested keys at 2 spaces, sequence dashes indented under the key.
    yaml.indent(mapping=2, sequence=4, offset=2)
    return yaml


def _is_developer_config(path: Path) -> bool:
    return path.name.lower() in _DEVELOPER_CONFIG_NAMES


def _sequence_trailing_token(seq):
    """Comment on the last sequence item, which ruamel uses for the next key."""
    items = getattr(getattr(seq, "ca", None), "items", None)
    if not items or not seq:
        return None
    slot = items.get(len(seq) - 1)
    if not slot:
        return None
    for index, part in enumerate(slot):
        if hasattr(part, "value") and isinstance(part.value, str) and part.value.strip():
            return part, slot, index
    return None


def _comment_token_after(mapping, key):
    """Return ``(token, slot, index)`` for the comment that trails ``key``.

    A block comment before the next key is stored on the previous key, often on
    the last nested key or the last sequence item. ``slot[index]`` is that token.
    """
    value = mapping[key]
    if isinstance(value, dict) and value:
        nested = _comment_token_after(value, next(reversed(value)))
        if nested is not None:
            return nested
    if isinstance(value, list) and value:
        trailing = _sequence_trailing_token(value)
        if trailing is not None:
            return trailing
    items = getattr(getattr(mapping, "ca", None), "items", None)
    if not items:
        return None
    slot = items.get(key)
    if slot and len(slot) > 2 and slot[2] is not None and hasattr(slot[2], "value"):
        return slot[2], slot, 2
    return None


def _split_eol_and_block(raw: str):
    """Split a same-line comment from the block comment that follows it.

    Returns ``(eol, block)``. ``eol`` is the same-line comment text including its
    trailing newline, or empty when the token is only a following block. ``block``
    is the comment body without ``#`` markers, or None when there is no block.
    """
    if "\n" not in raw:
        return raw, None
    eol, rest = raw.split("\n", 1)
    lines = []
    for line in rest.splitlines():
        stripped = line.strip()
        if not stripped:
            lines.append("")
            continue
        if not stripped.startswith("#"):
            return raw, None
        body = stripped[1:]
        if body.startswith(" "):
            body = body[1:]
        lines.append(body)
    while lines and lines[0] == "":
        lines.pop(0)
    while lines and lines[-1] == "":
        lines.pop()
    if not lines:
        return raw, None
    eol_text = f"{eol}\n" if eol else ""
    return eol_text, "\n".join(lines)


def _block_before_key(mapping, key) -> str | None:
    """Body of the block comment that sits in ``mapping`` just before ``key``."""
    keys = list(mapping.keys())
    index = keys.index(key)
    if index == 0:
        return None
    found = _comment_token_after(mapping, keys[index - 1])
    if found is None:
        return None
    token, _slot, _index = found
    _eol, block = _split_eol_and_block(token.value)
    return block


def _detach_block_before(mapping, later_key, indent: int) -> None:
    """Move a block comment off the previous key and onto ``later_key``.

    Otherwise inserting a key in front of ``later_key`` leaves that comment
    sitting above the new key.
    """
    if not hasattr(mapping, "yaml_set_comment_before_after_key"):
        return
    keys = list(mapping.keys())
    index = keys.index(later_key)
    if index == 0:
        return
    existing = mapping.ca.items.get(later_key) if hasattr(mapping, "ca") else None
    if existing and len(existing) > 1 and existing[1]:
        return
    found = _comment_token_after(mapping, keys[index - 1])
    if found is None:
        return
    token, slot, index = found
    eol, block = _split_eol_and_block(token.value)
    if not block:
        return
    if eol.strip():
        token.value = eol
    else:
        slot[index] = None
    mapping.yaml_set_comment_before_after_key(later_key, before=block, indent=indent)


def _has_before_comment(mapping, key) -> bool:
    slot = mapping.ca.items.get(key) if hasattr(mapping, "ca") else None
    return bool(slot and len(slot) > 1 and slot[1])


def _strip_trailing_block(node) -> str | None:
    """Remove the block comment that trails ``node`` and return its body.

    That comment introduces the next key in the template. Copied with the node,
    it would sit on top of the following section's own comment.
    """
    if not isinstance(node, dict) or not node:
        return None
    found = _comment_token_after(node, next(reversed(node)))
    if found is None:
        return None
    token, slot, index = found
    eol, block = _split_eol_and_block(token.value)
    if not block:
        return None
    if eol.strip():
        token.value = eol
    else:
        slot[index] = None
    return block


def _attach_block_comment(mapping, key, block: str | None, indent: int) -> None:
    if not block or not hasattr(mapping, "yaml_set_comment_before_after_key"):
        return
    if not block.startswith("\n"):
        block = "\n" + block
    mapping.yaml_set_comment_before_after_key(key, before=block, indent=indent)


def _insert_like_template(local, template, key, value, indent: int) -> None:
    """Insert ``key`` so it keeps its place relative to keys already in ``local``."""
    template_keys = list(template.keys())
    index = template_keys.index(key)
    block = _block_before_key(template, key)
    carried = _strip_trailing_block(value)
    if hasattr(local, "insert"):
        for later in template_keys[index + 1 :]:
            if later in local:
                _detach_block_before(local, later, indent)
                if carried and not _has_before_comment(local, later):
                    _attach_block_comment(local, later, carried, indent)
                local.insert(list(local.keys()).index(later), key, value)
                _attach_block_comment(local, key, block, indent)
                return
        for earlier in reversed(template_keys[:index]):
            if earlier in local:
                local.insert(list(local.keys()).index(earlier) + 1, key, value)
                _attach_block_comment(local, key, block, indent)
                return
    local[key] = value
    _attach_block_comment(local, key, block, indent)


def _add_missing_keys(local, template, prefix: str, added: list) -> None:
    """Add keys present in ``template`` and absent from ``local``. Existing values stay."""
    if not isinstance(local, dict) or not isinstance(template, dict):
        return
    indent = 0 if prefix == "" else 2
    for key, template_value in template.items():
        path = f"{prefix}.{key}" if prefix else str(key)
        if key not in local:
            _insert_like_template(local, template, key, deepcopy(template_value), indent)
            added.append(path)
            continue
        local_value = local[key]
        if isinstance(template_value, dict) and isinstance(local_value, dict):
            _add_missing_keys(local_value, template_value, path, added)


def sync_missing_template_keys(config_path: Path, config_data: dict, yaml: ruamel.yaml.YAML) -> list:
    """Fill keys missing from a developer config using the sibling template.

    Lists and scalars that already exist are left unchanged. The template file
    itself is never a sync target. Returns the dotted paths that were added.
    """
    if not _is_developer_config(config_path):
        return []
    template_path = config_path.parent / "config.template.YAML"
    if not template_path.is_file():
        return []
    with open(template_path, "r", encoding="utf-8") as handle:
        template_data = yaml.load(handle)
    if not isinstance(template_data, dict):
        return []
    added: list = []
    _add_missing_keys(config_data, template_data, "", added)
    return added


class ConfigLoader:
    """Handles loading and validation of YAML configuration files."""

    def __init__(self, yaml_path: str):
        """Initialize the config loader with path to YAML file.
        
        Args:
            yaml_path (str): Path to the configuration YAML file
        """
        self.config_file_path = Path(yaml_path)
        self.config_data = None

    def load(self):
        """Load and validate the YAML configuration file.
        
        Returns:
            dict: The loaded configuration data
        """
        if not self.config_file_path.is_file():
            raise FileNotFoundError(f"Configuration file not found: {self.config_file_path}")

        yaml = _round_trip_yaml()
        try:
            with open(self.config_file_path, "r", encoding="utf-8") as file:
                self.config_data = yaml.load(file)
        except ruamel.yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML format: {e}")
        except PermissionError as e:
            raise ValueError(f"Permission denied reading config file: {e}")

        if isinstance(self.config_data, dict):
            try:
                added = sync_missing_template_keys(self.config_file_path, self.config_data, yaml)
            except ruamel.yaml.YAMLError as e:
                raise ValueError(f"Invalid YAML format in config template: {e}")
            if added:
                with open(self.config_file_path, "w", encoding="utf-8", newline="\n") as handle:
                    yaml.dump(self.config_data, handle)
                logger.warning(
                    "config.yaml was missing keys from config.template.YAML; added defaults: %s",
                    ", ".join(added),
                )

        try:
            self._validate_config()
        except KeyError as e:
            raise ValueError(f"Missing required configuration key: {e}")
        
        return self.config_data

    def _validate_config(self):
        """Validate the configuration has all required fields."""
        # Check build_config section exists
        if 'build_config' not in self.config_data:
            raise KeyError("Missing required section: build_config")
        
        # Check required fields in build_config
        build_config_fields = [
            'write_dev',
            'write_vip',
            'target',
        ]
        
        for field in build_config_fields:
            if field not in self.config_data['build_config']:
                raise KeyError(f"Missing required field in build_config: {field}")
            
        # Check directories section exists
        if 'directories' not in self.config_data:
            raise KeyError("Missing required section: directories")
            
        # Check required directories exist
        required_dirs = [
            'warno_mods',
            'base_game',
            'base_vip',
            'gameplay_dev',
            'ui_only_dev',
            'gameplay_release',
            'ui_only_release',
            'vip_dev',
        ]
        
        for dir_field in required_dirs:
            if dir_field not in self.config_data['directories']:
                raise KeyError(f"Missing required directory: {dir_field}")

        # Validate asset configuration
        if 'asset_config' not in self.config_data:
            raise KeyError("Missing required section: asset_config")
        
        if 'target_dir' not in self.config_data['asset_config']:
            raise KeyError("Missing required field in asset_config: target_dir")

    def get(self, key, default=None):
        """Returns the value for the given key, or default if not found."""
        if self.config_data is None:
            raise ValueError("Config data is not loaded. Call load() first.")
        return self.config_data.get(key, default)

    def get_directories(self):
        """Get the directories section of the configuration."""
        return self.get("directories", {})

    def get_write_dev(self):
        """Effective development-build flag. write_vip forces this on."""
        build_config = self.get("build_config", {})
        if build_config.get("write_vip"):
            return True
        return build_config.get("write_dev", False)


def load_config(config_path: str = None) -> dict:
    """Load configuration from the specified path or default location.
    
    Args:
        config_path (str, optional): Path to config file. If None, uses default location.
        
    Returns:
        dict: The loaded configuration data
    """
    if config_path is None:
        # Look for config file in common locations
        possible_paths = [
            "config/config.YAML",
            "config/config.yaml", 
            "config/config.yml"
        ]
        
        for path in possible_paths:
            if Path(path).exists():
                config_path = path
                break
        else:
            raise FileNotFoundError("No configuration file found. Please create config/config.YAML")
    
    loader = ConfigLoader(config_path)
    return loader.load()
