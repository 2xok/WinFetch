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

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/2xok/WinFetch.git
   cd WinFetch
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run WinFetch:**
   ```bash
   # Easy way (recommended)
   winfetch.bat
   
   # Or using PowerShell
   .\winfetch.ps1
   
   # Or directly with Python
   python main.py
   ```

## Usage

### Easy Launchers

WinFetch includes convenient launcher scripts that automatically find your Python installation:

- **`winfetch.bat`** - Windows batch file (works in CMD and PowerShell)
- **`winfetch.ps1`** - PowerShell script with better error handling

### Basic Usage

```bash
# Display system info with default ASCII art
winfetch.bat
# or
.\winfetch.ps1
# or
python main.py

# Use a specific built-in ASCII art
winfetch.bat --ascii-art windows_simple

# Use custom ASCII art from file
winfetch.bat --ascii-art /path/to/your/art.txt

# Disable colors
winfetch.bat --no-color

# List available built-in ASCII arts
winfetch.bat --list-arts

# Show version information
winfetch.bat --version
```

### Command Line Options

| Option | Description |
|--------|-------------|
| `-a, --ascii-art` | Specify ASCII art file or built-in name |
| `-c, --config` | Path to custom configuration file |
| `--no-color` | Disable colored output |
| `--list-arts` | List available built-in ASCII art options |
| `-v, --version` | Show version information |

## Built-in ASCII Art

WinFetch comes with several built-in ASCII art designs:

- `windows` - Default Windows logo design
- `windows_simple` - Simple Windows logo

View all available options with:
```bash
winfetch.bat --list-arts
```

## Configuration

WinFetch creates a configuration file at: `%LOCALAPPDATA%\winfetch\config.yaml`

You can customize:
- Colors and color schemes
- Which system information to display
- Default ASCII art
- And more!

## System Information Displayed

WinFetch shows comprehensive system information using Windows-specific APIs:

- **User & Hostname** - Current user and computer name
- **OS** - Windows edition and build number (via WMI)
- **Kernel** - Windows kernel version
- **Uptime** - System uptime since last boot
- **Shell** - Current shell (CMD, PowerShell, etc.)
- **Terminal** - Terminal emulator detection
- **CPU** - Processor name, cores, and threads (via WMI)
- **GPU** - Graphics card information (via WMI)
- **Memory** - RAM usage and total capacity
- **Disk** - System drive usage (C:)
- **Network** - Active network interfaces and IP addresses

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
