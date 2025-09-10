"""
Main display engine to render ASCII art and system information side-by-side.
"""
from pathlib import Path
from typing import List
from colorama import init as colorama_init, Fore, Style

from .sysinfo import SystemInfo
from .ascii_art import AsciiArtLoader


class WinFetchDisplay:
    def __init__(self, config_manager, args):
        colorama_init()
        self.config = config_manager.load()
        self.args = args
        self.sysinfo = SystemInfo()
        self.art_loader = AsciiArtLoader(Path(__file__).parent.parent / "ascii_art")
        self.colors_enabled = not args.no_color and self.config.get("colors", True)

    def list_available_arts(self):
        arts = self.art_loader.list_builtins()
        if not arts:
            print("No built-in ASCII arts found.")
            return
        print("Available built-in ASCII arts:")
        for name in arts:
            print(f" - {name}")

    def show(self):
        # Load ASCII art
        try:
            art = self.art_loader.load(self.args.ascii_art or self.config.get("ascii_art"))
            art_lines = art.splitlines()
        except Exception as e:
            # Fallback to simple ASCII art
            art_lines = [
                "    ╔══════════════════════╗",
                "    ║      WINFETCH        ║",
                "    ║                      ║",
                "    ║    ██████████████    ║",
                "    ║    ██████████████    ║",
                "    ║    ██████████████    ║",
                "    ║                      ║",
                "    ╚══════════════════════╝"
            ]
        
        # Collect system info
        info = self.sysinfo.get_all_info()
        info_lines = self._format_info_lines(info)

        # Compute layout: side-by-side
        left_width = max((len(line) for line in art_lines), default=0) + 4
        for i in range(max(len(art_lines), len(info_lines))):
            left = art_lines[i] if i < len(art_lines) else ""
            right = info_lines[i] if i < len(info_lines) else ""
            print(f"{left:<{left_width}}{right}")

    def _format_info_lines(self, info: dict) -> List[str]:
        pairs = [
            ("User", f"{info['user']}@{info['hostname']}"),
            ("OS", info['os']),
            ("Kernel", info['kernel']),
            ("Uptime", info['uptime']),
            ("Shell", info['shell']),
            ("Terminal", info['terminal']),
            ("CPU", info['cpu']),
            ("GPU", ", ".join(info.get('gpu', ['Unknown']))),
            ("Memory", info['memory']),
            ("Disk", info['disk']),
        ]
        
        # Optional: network lines
        if info.get('network'):
            for idx, net in enumerate(info['network'], start=1):
                pairs.append((f"Net{idx}", net))

        lines = []
        for key, value in pairs:
            k = self._colorize(key, Fore.CYAN)
            v = self._colorize(value, Fore.WHITE)
            lines.append(f"{k}: {v}")
        return lines

    def _colorize(self, text: str, color):
        if self.colors_enabled:
            return f"{color}{text}{Style.RESET_ALL}"
        return text
