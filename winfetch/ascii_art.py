"""
ASCII art loading system.
"""
from pathlib import Path
from typing import Optional, List


class AsciiArtLoader:
    """Load ASCII art from built-ins or user-provided files."""

    def __init__(self, builtins_dir: Path):
        self.builtins_dir = builtins_dir

    def list_builtins(self) -> List[str]:
        if not self.builtins_dir.exists():
            return []
        return [p.stem for p in self.builtins_dir.glob("*.txt")]

    def load(self, name_or_path: Optional[str]) -> str:
        """Load ASCII art by name (builtin) or by file path."""
        if not name_or_path:
            # Default art
            name_or_path = "windows"
        
        p = Path(name_or_path)
        if p.exists():
            return p.read_text(encoding="utf-8", errors="ignore")
        
        # Try builtin
        builtin_path = self.builtins_dir / f"{name_or_path}.txt"
        if builtin_path.exists():
            return builtin_path.read_text(encoding="utf-8", errors="ignore")
        
        raise FileNotFoundError(f"ASCII art '{name_or_path}' not found. Use --list-arts to see options.")
