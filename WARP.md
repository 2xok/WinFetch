# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

WinFetch is a Windows system information display tool inspired by neofetch, built in Python. It displays system information alongside customizable ASCII art in the terminal, optimized for Windows platforms.

## Development Commands

### Basic Commands
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application (easy way)
winfetch.bat
# or
.\winfetch.ps1
# or directly
python main.py

# Run with specific ASCII art
winfetch.bat --ascii-art windows_simple

# List available built-in ASCII arts
winfetch.bat --list-arts

# Disable colors
winfetch.bat --no-color

# Show version
winfetch.bat --version

# Use custom config file
winfetch.bat --config path/to/config.yaml
```

### Testing & Development
```bash
# Install in development mode
pip install -e .

# Check if all modules import correctly
python -c "from winfetch import display, sysinfo, config_manager, ascii_art; print('All imports successful')"
```

### Package Management
```bash
# Create distribution packages
python setup.py sdist bdist_wheel

# Install from local package
pip install .
```

## Current Development Status

✅ **Status**: Core functionality is working and ready for use!

Completed components:
- `winfetch/display.py` ✅ Display engine with side-by-side rendering
- `winfetch/sysinfo.py` ✅ System information collection using Windows APIs  
- `winfetch/config_manager.py` ✅ Configuration management with YAML support
- `winfetch/ascii_art.py` ✅ ASCII art loading system
- `ascii_art/` directory ✅ Built-in ASCII art files
- `winfetch.bat` ✅ Windows batch launcher
- `winfetch.ps1` ✅ PowerShell launcher script

Still needed:
- `setup.py` - Package setup script for pip installation
- Additional ASCII art designs
- Comprehensive test suite

## Architecture Overview

### Core Components (When Complete)

**Main Entry Point (`main.py`)** ✅
- Command-line argument parsing
- Application initialization and error handling
- Coordinates between display, config, and system info components

**Display Engine (`winfetch/display.py`)** ❌ *Needs recreation*
- `WinFetchDisplay` class orchestrates the main output rendering
- Handles side-by-side layout of ASCII art and system information
- Manages color output based on configuration and command-line flags

**System Information (`winfetch/sysinfo.py`)** ❌ *Needs recreation*
- `SystemInfo` class provides comprehensive Windows system data
- Uses multiple APIs: WMI, psutil, pywin32, and platform modules
- Graceful fallbacks when optional dependencies are unavailable

**Configuration Management (`winfetch/config_manager.py`)** ❌ *Needs recreation*
- `ConfigManager` handles YAML configuration files with fallbacks
- Default config location: `%LOCALAPPDATA%\winfetch\config.yaml`

**ASCII Art System (`winfetch/ascii_art.py`)** ❌ *Needs recreation*
- `AsciiArtLoader` manages built-in and custom ASCII art
- Built-in arts located in `ascii_art/` directory

### Immediate Development Priorities

1. Recreate core module files
2. Add ASCII art collection
3. Implement proper error handling and fallbacks
4. Test all functionality on Windows systems
5. Add comprehensive test suite

## Dependencies

**Required Dependencies**:
- `colorama`: Cross-platform terminal colors
- `psutil`: System and process information

**Optional Dependencies** (with graceful fallbacks):
- `wmi`: Windows Management Instrumentation (enhanced system info)
- `pywin32`: Windows API access (additional system details)
- `pyyaml`: YAML configuration parsing
