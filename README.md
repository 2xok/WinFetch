# WinFetch

A customizable Windows system information display tool inspired by neofetch/fastfetch. WinFetch displays system information alongside beautiful ASCII art in your terminal.

## Features

- 🎨 **Customizable ASCII Art** - Choose from built-in designs or use your own custom ASCII art
- 🖥️ **Comprehensive System Info** - Shows OS, CPU, GPU, memory, disk usage, and more
- 🌈 **Colorful Output** - Beautiful colored terminal output with customizable color schemes
- ⚙️ **Highly Configurable** - Extensive configuration options via YAML files
- 🚀 **Windows Optimized** - Uses Windows-specific APIs for accurate system information
- 💾 **Lightweight** - Fast startup and minimal resource usage

## Installation

### Prerequisites

- Python 3.7 or higher
- Windows 10/11 (designed specifically for Windows)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run WinFetch

```bash
python main.py
```

## Usage

### Basic Usage

```bash
# Display system info with default ASCII art
python main.py

# Use a specific built-in ASCII art
python main.py --ascii-art windows_simple

# Use custom ASCII art from file
python main.py --ascii-art /path/to/your/art.txt

# Disable colors
python main.py --no-color

# List available built-in ASCII arts
python main.py --list-arts
```

## Development Status

🚧 **This project is currently being prepared for open source release** 🚧

Some files may be missing or incomplete. The core functionality is working, but we're in the process of organizing the codebase for public contribution.

## Contributing

We welcome contributions! Please check back soon for detailed contribution guidelines.

## License

This project is licensed under the MIT License.

## Inspiration

WinFetch is inspired by:
- [neofetch](https://github.com/dylanaraps/neofetch) - The original system info tool
- [fastfetch](https://github.com/fastfetch-cli/fastfetch) - Fast neofetch alternative

---

Made with ❤️ for Windows users who love beautiful terminals!
