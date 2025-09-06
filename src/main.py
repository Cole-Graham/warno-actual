"""Main entry point for the mod patcher."""

# from typing import Dict
import re
import inspect

from . import ModConfig, ndf
from .editors import get_all_editors
from .utils.asset_utils import copy_assets
from .utils.config_utils import get_mod_dst_path, get_mod_src_path
from .utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def get_editor_name(editor):
    """Extract a meaningful name for the editor function, handling lambda wrappers."""
    # If it's a lambda, try to extract the function name from the source code
    if hasattr(editor, "__name__") and editor.__name__ == "<lambda>":
        try:
            # Get the source code of the lambda
            source = inspect.getsource(editor)
            # Look for function calls in the lambda
            # Common patterns: function_name(source_path, game_db) or function_name(source_path)
            import re

            # Match function calls in the lambda
            func_matches = re.findall(r"(\w+)\(source_path", source)
            if func_matches:
                return func_matches[0]  # Return the first function name found
            # Fallback: try to get the full lambda expression
            lambda_match = re.search(r"lambda\s+\w+:\s*(\w+)\(", source)
            if lambda_match:
                return lambda_match.group(1)
        except (OSError, TypeError):
            pass
        # If we can't extract the name, return a generic lambda identifier
        return "<lambda>"

    # For regular functions, return the function name
    if hasattr(editor, "__name__"):
        return editor.__name__

    # Try to get __qualname__ for lambdas or partials
    if hasattr(editor, "__qualname__"):
        return editor.__qualname__

    # Try to get the function attribute for functools.partial or similar
    if hasattr(editor, "func"):
        return get_editor_name(editor.func)

    # Try to get __wrapped__ for decorated functions
    if hasattr(editor, "__wrapped__"):
        return get_editor_name(editor.__wrapped__)

    # Fallback to repr
    return repr(editor)


def main() -> None:
    """Run the mod patcher."""
    try:
        config = ModConfig.get_instance().config_data

        # Get paths and initialize mod
        mod_src_path = get_mod_src_path(config)
        mod_dst_path = get_mod_dst_path(config)
        mod = ndf.Mod(str(mod_src_path), str(mod_dst_path))
        mod.check_if_src_is_newer()

        # Get all file editors based on build target
        editors = get_all_editors(config)

        # Process each file
        build_target_cfg = config["build_config"]["target"]
        for file_path, editor_list in editors.items():
            if not editor_list:  # Skip empty editor lists
                continue

            try:
                with mod.edit(file_path) as source:
                    for editor, build_target in editor_list:
                        
                        if build_target_cfg == "ui_only" and build_target == "ui":
                            logger.info(f"Processing {file_path}")
                            try:
                                editor(source)
                            except Exception as e:
                                logger.error(f"Editor failed for {file_path}: {str(e)}")
                                raise
                        
                        # Logging skipped entries for ui_only build target configuration
                        elif build_target_cfg == "ui_only" and build_target == "gameplay":
                            # Regex to match everything up to the last '/' in the string
                            path_replacement_regex = r"^.*/"

                            editor_name = get_editor_name(editor)
                            logger.info(
                                f"Skipping {re.sub(path_replacement_regex, '', file_path)} editor: {editor_name} with build target {build_target}",
                            )
                            continue

                        elif build_target_cfg == "gameplay":
                            logger.info(f"Processing {file_path}")
                            try:
                                editor(source)
                            except Exception as e:
                                logger.error(f"Editor failed for {file_path}: {str(e)}")
                                raise

                        else:
                            logger.warning(
                                f"config build target: {build_target_cfg}, "
                                f"editor build target: {build_target}\n"
                                f"Invalid configuration. Skipping editor for {file_path}\n"
                            )

            except Exception as e:
                logger.error(f"Failed processing {file_path}: {str(e)}")
                raise

        # Copy assets
        copy_assets(config)

        logger.info("Build completed successfully")

    except Exception as e:
        logger.error(f"Build failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
