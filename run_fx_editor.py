"""Entry point script for FX Editor."""

import sys
from pathlib import Path

# Add project root to path for src imports
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

if __name__ == '__main__':
    from tools.fx_editor.main import main
    main()
