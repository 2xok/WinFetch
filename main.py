#!/usr/bin/env python3
"""
WinFetch - Main entry point
"""

import sys
import argparse
from pathlib import Path

# Add the winfetch package to the path
sys.path.insert(0, str(Path(__file__).parent))

from winfetch.display import WinFetchDisplay
from winfetch.config_manager import ConfigManager


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="WinFetch - A Windows system information display tool",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--ascii-art", "-a",
        type=str,
        help="Path to custom ASCII art file or name of built-in art"
    )
    
    parser.add_argument(
        "--config", "-c",
        type=str,
        help="Path to custom configuration file"
    )
    
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored output"
    )
    
    parser.add_argument(
        "--list-arts",
        action="store_true",
        help="List available built-in ASCII art options"
    )
    
    parser.add_argument(
        "--version", "-v",
        action="store_true",
        help="Show version information"
    )
    
    return parser.parse_args()


def main():
    """Main entry point."""
    args = parse_arguments()
    
    if args.version:
        from winfetch import __version__
        print(f"WinFetch v{__version__}")
        return
    
    try:
        # Initialize configuration
        config_manager = ConfigManager(args.config)
        
        # Initialize display
        display = WinFetchDisplay(config_manager, args)
        
        if args.list_arts:
            display.list_available_arts()
            return
        
        # Run the main display
        display.show()
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
