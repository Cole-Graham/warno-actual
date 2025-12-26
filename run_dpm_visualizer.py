"""Entry point script for DPM Visualizer."""

import sys
from pathlib import Path

# Add project root to path for src imports
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Import and run the visualizer
if __name__ == "__main__":
    # Import here to ensure path is set
    from tools.dpm_visualizer.main import main
    main()

