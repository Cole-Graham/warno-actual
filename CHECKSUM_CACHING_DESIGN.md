# Checksum-Based Caching System Design

## Overview

This document outlines the design and implementation plan for a checksum-based caching system that will skip file processing when editor inputs haven't changed, significantly improving development iteration speed.

## Problem Statement

The WARNO patcher currently processes 50+ files on every run, even when only small changes are made. This creates long wait times during development and testing. A caching system that skips unchanged files would dramatically improve developer experience.

## Architecture Overview

### Core Concept
- Generate checksums for each editor's inputs (code, constants, database, config)
- Store checksums from previous runs
- Skip editors whose inputs haven't changed
- Provide force rebuild option to bypass caching

### System Components
1. **Checksum Calculator**: Generates checksums for editor inputs
2. **Cache Manager**: Stores and retrieves checksums
3. **Dependency Analyzer**: Determines what data each editor depends on
4. **Main Loop Integration**: Checksums before running editors

## Editor Classification

### Type 1: Static Editors (No External Dependencies)
**Examples:**
- `edit_gameplay_constantes_gdconstants`
- `edit_gameplay_terrains`
- Most UI style editors

**Dependencies:** Only editor function code
**Checksum:** MD5 of function source code

### Type 2: Constants-Dependent Editors
**Examples:**
- `edit_gen_gp_gfx_depictionvehicles`
- `edit_gen_gp_gfx_depictioninfantry`
- Most depiction editors

**Dependencies:** Editor code + constants (NEW_UNITS, NEW_DEPICTIONS, etc.)
**Checksum:** MD5 of (code + relevant constants)

### Type 3: Database-Dependent Editors
**Examples:**
- `edit_gen_gp_gfx_unitedescriptor`
- `edit_gen_gp_decks_divisions`
- `edit_gen_gp_decks_strategicdecks`

**Dependencies:** Editor code + constants + relevant game_db data
**Checksum:** MD5 of (code + constants + relevant database sections)

## Implementation Plan

### Phase 1: Foundation (Static Editors)
**Goal:** Implement caching for editors with no external dependencies

**Components:**
1. `src/utils/checksum_utils.py` - Core checksum functions
2. `src/data/editor_checksums.json` - Checksum storage
3. Basic cache manager

**Files to Create:**
```
src/utils/checksum_utils.py
src/data/editor_checksums.json (auto-generated)
```

**Configuration Changes:**
```yaml
# config/config.YAML
build_config:
  enable_checksum_cache: true
  force_rebuild: false
```

### Phase 2: Constants Integration
**Goal:** Add support for constants-dependent editors

**Components:**
1. Dependency analyzer for constants
2. Constants checksum calculation
3. Cache invalidation on constants changes

### Phase 3: Database Integration
**Goal:** Add support for database-dependent editors

**Components:**
1. Database section checksum calculation
2. Selective database checksumming
3. Integration with existing database system

### Phase 4: Advanced Features
**Goal:** Polish and optimization

**Components:**
1. Cache cleanup and management
2. Performance monitoring
3. Debug tools and logging

## Detailed Implementation

### 1. Checksum Utilities (`src/utils/checksum_utils.py`)

```python
"""Checksum calculation utilities for editor caching."""

import hashlib
import inspect
import json
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set, Tuple
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

class EditorChecksumCalculator:
    """Calculates checksums for editor functions and their dependencies."""
    
    def __init__(self):
        self._constants_cache = {}
        self._dependency_cache = {}
    
    def get_editor_code_checksum(self, editor_func: Callable) -> str:
        """Get checksum of editor function source code."""
        try:
            source_code = inspect.getsource(editor_func)
            return hashlib.md5(source_code.encode()).hexdigest()
        except (OSError, TypeError):
            # Handle lambda functions or functions without source
            return hashlib.md5(str(editor_func).encode()).hexdigest()
    
    def get_constants_checksum(self, editor_func: Callable) -> str:
        """Get checksum of constants data used by editor."""
        source_code = inspect.getsource(editor_func)
        checksum_data = []
        
        # Check for NEW_UNITS usage
        if 'NEW_UNITS' in source_code:
            checksum_data.append(self._get_new_units_checksum())
        
        # Check for unit_edits usage
        if 'load_unit_edits' in source_code or 'unit_edits' in source_code:
            checksum_data.append(self._get_unit_edits_checksum())
        
        # Check for NEW_DEPICTIONS usage
        if 'NEW_DEPICTIONS' in source_code:
            checksum_data.append(self._get_new_depictions_checksum())
        
        # Add other constants as needed...
        
        combined_data = '|'.join(checksum_data)
        return hashlib.md5(combined_data.encode()).hexdigest()
    
    def get_game_db_checksum(self, game_db: Dict, editor_func: Callable) -> str:
        """Get checksum of relevant game_db data for this editor."""
        source_code = inspect.getsource(editor_func)
        relevant_data = {}
        
        # Determine which parts of game_db this editor uses
        if 'game_db["unit_data"]' in source_code:
            relevant_data['unit_data'] = game_db.get('unit_data', {})
        
        if 'game_db["decks"]' in source_code:
            relevant_data['decks'] = game_db.get('decks', {})
        
        if 'game_db["weapons"]' in source_code:
            relevant_data['weapons'] = game_db.get('weapons', {})
        
        if 'game_db["depiction_data"]' in source_code:
            relevant_data['depiction_data'] = game_db.get('depiction_data', {})
        
        # Convert to string and hash
        data_str = str(sorted(relevant_data.items()))
        return hashlib.md5(data_str.encode()).hexdigest()
    
    def get_config_checksum(self, config: Dict, editor_func: Callable) -> str:
        """Get checksum of relevant config data."""
        source_code = inspect.getsource(editor_func)
        relevant_config = {
            'build_target': config.get('build_config', {}).get('target'),
            'write_dev': config.get('build_config', {}).get('write_dev'),
        }
        
        # Add other config values that affect this editor
        if 'hide_divs' in source_code:
            relevant_config['hide_divs'] = config.get('hide_divs', [])
        
        config_str = str(sorted(relevant_config.items()))
        return hashlib.md5(config_str.encode()).hexdigest()
    
    def calculate_editor_checksum(self, editor_func: Callable, game_db: Dict, config: Dict) -> str:
        """Calculate combined checksum for an editor."""
        checksums = [
            self.get_editor_code_checksum(editor_func),
            self.get_constants_checksum(editor_func),
            self.get_game_db_checksum(game_db, editor_func),
            self.get_config_checksum(config, editor_func),
        ]
        
        # Combine all checksums
        combined = '|'.join(checksums)
        return hashlib.md5(combined.encode()).hexdigest()
    
    def _get_new_units_checksum(self) -> str:
        """Get checksum of NEW_UNITS constant."""
        if 'NEW_UNITS' not in self._constants_cache:
            from src.constants.new_units import NEW_UNITS
            self._constants_cache['NEW_UNITS'] = hashlib.md5(
                str(sorted(NEW_UNITS.items())).encode()
            ).hexdigest()
        return self._constants_cache['NEW_UNITS']
    
    def _get_unit_edits_checksum(self) -> str:
        """Get checksum of unit_edits data."""
        if 'unit_edits' not in self._constants_cache:
            from src.constants.unit_edits import load_unit_edits
            unit_edits = load_unit_edits()
            self._constants_cache['unit_edits'] = hashlib.md5(
                str(sorted(unit_edits.items())).encode()
            ).hexdigest()
        return self._constants_cache['unit_edits']
    
    def _get_new_depictions_checksum(self) -> str:
        """Get checksum of NEW_DEPICTIONS constant."""
        if 'NEW_DEPICTIONS' not in self._constants_cache:
            from src.constants.new_units.new_depictions import NEW_DEPICTIONS
            self._constants_cache['NEW_DEPICTIONS'] = hashlib.md5(
                str(sorted(NEW_DEPICTIONS.items())).encode()
            ).hexdigest()
        return self._constants_cache['NEW_DEPICTIONS']


class EditorCacheManager:
    """Manages editor checksum cache storage and retrieval."""
    
    def __init__(self, cache_file: Path):
        self.cache_file = cache_file
        self.cache_data = self._load_cache()
    
    def _load_cache(self) -> Dict:
        """Load cache from disk."""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f"Failed to load cache file: {e}")
        return {}
    
    def _save_cache(self) -> None:
        """Save cache to disk."""
        try:
            self.cache_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.cache_file, 'w') as f:
                json.dump(self.cache_data, f, indent=2)
        except IOError as e:
            logger.error(f"Failed to save cache file: {e}")
    
    def get_editor_checksum(self, file_path: str, editor_name: str) -> Optional[str]:
        """Get stored checksum for an editor."""
        key = f"{file_path}:{editor_name}"
        return self.cache_data.get(key, {}).get('checksum')
    
    def set_editor_checksum(self, file_path: str, editor_name: str, checksum: str) -> None:
        """Store checksum for an editor."""
        key = f"{file_path}:{editor_name}"
        self.cache_data[key] = {
            'checksum': checksum,
            'timestamp': str(Path().cwd().stat().st_mtime)  # Simple timestamp
        }
        self._save_cache()
    
    def clear_cache(self) -> None:
        """Clear all cached checksums."""
        self.cache_data = {}
        self._save_cache()
    
    def get_cache_stats(self) -> Dict:
        """Get cache statistics."""
        return {
            'total_entries': len(self.cache_data),
            'cache_file_size': self.cache_file.stat().st_size if self.cache_file.exists() else 0
        }


def should_skip_editor(
    file_path: str, 
    editor_func: Callable, 
    editor_name: str,
    game_db: Dict, 
    config: Dict,
    cache_manager: EditorCacheManager,
    calculator: EditorChecksumCalculator
) -> bool:
    """Determine if an editor should be skipped based on checksum."""
    
    # Check if caching is enabled
    if not config.get('build_config', {}).get('enable_checksum_cache', True):
        return False
    
    # Check if force rebuild is enabled
    if config.get('build_config', {}).get('force_rebuild', False):
        return False
    
    try:
        # Calculate current checksum
        current_checksum = calculator.calculate_editor_checksum(editor_func, game_db, config)
        
        # Get stored checksum
        stored_checksum = cache_manager.get_editor_checksum(file_path, editor_name)
        
        if stored_checksum == current_checksum:
            logger.info(f"Skipping {editor_name} for {file_path} - no changes detected")
            return True
        
        # Update cache with new checksum
        cache_manager.set_editor_checksum(file_path, editor_name, current_checksum)
        return False
        
    except Exception as e:
        logger.warning(f"Checksum calculation failed for {editor_name}: {e}")
        return False  # Run editor on error
```

### 2. Main Loop Integration (`src/main.py` modifications)

```python
# Add to imports
from src.utils.checksum_utils import EditorChecksumCalculator, EditorCacheManager, should_skip_editor

def main() -> None:
    """Run the mod patcher."""
    try:
        config = ModConfig.get_instance().config_data

        # Get paths and initialize mod
        mod_src_path = get_mod_src_path(config)
        mod_dst_path = get_mod_dst_path(config)
        mod = ndf.Mod(str(mod_src_path), str(mod_dst_path))
        mod.check_if_src_is_newer()

        # Initialize checksum system
        cache_file = Path("src/data/editor_checksums.json")
        cache_manager = EditorCacheManager(cache_file)
        calculator = EditorChecksumCalculator()
        
        # Get all file editors based on build target
        editors = get_all_editors(config)
        game_db = config.get("game_db", {})

        # Process each file
        build_target_cfg = config["build_config"]["target"]
        skipped_count = 0
        processed_count = 0
        
        for file_path, editor_list in editors.items():
            if not editor_list:  # Skip empty editor lists
                continue

            try:
                with mod.edit(file_path) as source:
                    for editor, build_target in editor_list:
                        
                        # Check if we should skip this editor
                        editor_name = get_editor_name(editor)
                        if should_skip_editor(file_path, editor, editor_name, game_db, config, cache_manager, calculator):
                            skipped_count += 1
                            continue
                        
                        # Process editor based on build target
                        if build_target_cfg == "ui_only" and build_target == "ui":
                            logger.info(f"Processing {file_path}")
                            try:
                                editor(source)
                                processed_count += 1
                            except Exception as e:
                                logger.error(f"Editor failed for {file_path}: {str(e)}")
                                raise
                        
                        # ... rest of existing logic ...
                        
            except Exception as e:
                logger.error(f"Failed processing {file_path}: {str(e)}")
                raise

        # Log cache statistics
        logger.info(f"Cache stats: {processed_count} processed, {skipped_count} skipped")
        logger.info(f"Cache performance: {cache_manager.get_cache_stats()}")

        # Copy assets and create new .ndf asset definitions.
        add_unit_meshes(config)
        copy_assets(config)

        logger.info("Build completed successfully")

    except Exception as e:
        logger.error(f"Build failed: {str(e)}")
        raise
```

### 3. Configuration Updates (`config/config.YAML`)

```yaml
# Build configuration
build_config:
  write_dev: true
  target: "gameplay"
  enable_checksum_cache: true  # Enable/disable checksum caching
  force_rebuild: false         # Force rebuild all files, bypassing cache

# Data configuration
data_config:
  build_database: false
  database_path: "src/data/database"
  update_master_metadata: false

# ... rest of existing config ...
```

## Testing Strategy

### Unit Tests
1. **Checksum Calculator Tests**
   - Test checksum generation for different editor types
   - Test checksum consistency across runs
   - Test checksum changes when inputs change

2. **Cache Manager Tests**
   - Test cache storage and retrieval
   - Test cache invalidation
   - Test cache file corruption handling

3. **Integration Tests**
   - Test full patcher run with caching enabled
   - Test cache hit/miss scenarios
   - Test force rebuild functionality

### Performance Tests
1. **Benchmark Tests**
   - Measure time savings with caching
   - Compare memory usage with/without caching
   - Test cache file size growth

2. **Stress Tests**
   - Test with large numbers of editors
   - Test cache performance with large constants
   - Test database checksum performance

## Migration Strategy

### Phase 1: Foundation (Week 1-2)
1. Implement `checksum_utils.py`
2. Add basic cache manager
3. Integrate with static editors only
4. Add configuration options
5. Test with simple editors

### Phase 2: Constants Integration (Week 3-4)
1. Add constants dependency analysis
2. Implement constants checksum calculation
3. Test with constants-dependent editors
4. Add cache invalidation on constants changes

### Phase 3: Database Integration (Week 5-6)
1. Add database section checksum calculation
2. Integrate with existing database system
3. Test with database-dependent editors
4. Optimize database checksum performance

### Phase 4: Polish (Week 7-8)
1. Add comprehensive logging
2. Implement cache cleanup tools
3. Add performance monitoring
4. Create documentation
5. Final testing and optimization

## Risk Assessment

### High Risk
- **Cache corruption**: Could lead to skipped necessary updates
- **Performance regression**: Checksum calculation overhead
- **Complexity**: System becomes harder to debug

### Medium Risk
- **Memory usage**: Caching large constants/database sections
- **File system issues**: Cache file permissions/corruption
- **Dependency analysis**: Incorrect detection of editor dependencies

### Low Risk
- **Configuration changes**: New config options
- **Logging changes**: Additional log messages

### Mitigation Strategies
1. **Fallback behavior**: Always run editors on checksum errors
2. **Force rebuild option**: Bypass cache when needed
3. **Comprehensive logging**: Track cache hits/misses
4. **Incremental rollout**: Start with simple editors
5. **Extensive testing**: Unit and integration tests

## Success Metrics

### Performance Metrics
- **Time savings**: 50-80% reduction in patcher runtime for unchanged files
- **Cache hit rate**: 70-90% for typical development scenarios
- **Memory overhead**: <10% increase in memory usage

### Quality Metrics
- **Zero false positives**: No skipped necessary updates
- **Zero false negatives**: No unnecessary runs
- **Reliability**: 99.9% cache accuracy

### Developer Experience
- **Faster iteration**: Sub-second runs for small changes
- **Transparency**: Clear logging of cache decisions
- **Control**: Easy cache management and force rebuild

## Future Enhancements

### Advanced Features
1. **Incremental caching**: Cache partial results
2. **Parallel processing**: Run independent editors in parallel
3. **Smart invalidation**: Only invalidate affected editors
4. **Cache compression**: Reduce cache file size
5. **Distributed caching**: Share cache across team members

### Monitoring and Analytics
1. **Performance dashboards**: Track cache performance over time
2. **Usage analytics**: Identify most/least cached editors
3. **Optimization suggestions**: Recommend cache improvements
4. **Alert system**: Notify on cache issues

## Conclusion

The checksum-based caching system will significantly improve developer experience by reducing patcher runtime for unchanged files. The phased implementation approach minimizes risk while providing immediate benefits. The system is designed to be robust, with fallback mechanisms and comprehensive testing to ensure reliability.

The investment in this system will pay dividends in improved development velocity and reduced frustration during the development and testing process.
