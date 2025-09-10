"""
System information detection module for Windows.
"""

import platform
import socket
import os
import subprocess
import psutil
from pathlib import Path
import time

try:
    import wmi
    WMI_AVAILABLE = True
except ImportError:
    WMI_AVAILABLE = False

try:
    import win32api
    import win32con
    import win32file
    WIN32_AVAILABLE = True
except ImportError:
    WIN32_AVAILABLE = False


class SystemInfo:
    """Collect system information on Windows."""
    
    def __init__(self):
        """Initialize system info collector."""
        self._wmi_conn = None
        if WMI_AVAILABLE:
            try:
                self._wmi_conn = wmi.WMI()
            except Exception:
                pass

    def get_all_info(self):
        """Get all system information as a dictionary."""
        return {
            'user': self.get_user(),
            'hostname': self.get_hostname(),
            'os': self.get_os_info(),
            'kernel': self.get_kernel(),
            'uptime': self.get_uptime(),
            'packages': self.get_packages(),
            'shell': self.get_shell(),
            'terminal': self.get_terminal(),
            'cpu': self.get_cpu(),
            'memory': self.get_memory(),
            'gpu': self.get_gpu(),
            'disk': self.get_disk_usage(),
            'network': self.get_network_info(),
        }

    def get_user(self):
        """Get current username."""
        return os.getenv('USERNAME', 'Unknown')

    def get_hostname(self):
        """Get computer hostname."""
        return socket.gethostname()

    def get_os_info(self):
        """Get OS information."""
        try:
            # Try to get detailed Windows version info
            if self._wmi_conn:
                for os_info in self._wmi_conn.Win32_OperatingSystem():
                    version = os_info.Version
                    build = os_info.BuildNumber
                    edition = os_info.Caption
                    return f"{edition} (Build {build})"
            
            # Fallback to platform module
            return f"{platform.system()} {platform.release()}"
        except Exception:
            return f"{platform.system()} {platform.release()}"

    def get_kernel(self):
        """Get kernel version."""
        return platform.version()

    def get_uptime(self):
        """Get system uptime."""
        try:
            boot_time = psutil.boot_time()
            uptime_seconds = time.time() - boot_time
            
            days = int(uptime_seconds // 86400)
            hours = int((uptime_seconds % 86400) // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            
            if days > 0:
                return f"{days}d {hours}h {minutes}m"
            elif hours > 0:
                return f"{hours}h {minutes}m"
            else:
                return f"{minutes}m"
        except Exception:
            return "Unknown"

    def get_packages(self):
        """Get installed packages count."""
        try:
            # Try to count installed Windows programs via WMI
            if self._wmi_conn:
                programs = list(self._wmi_conn.Win32_Product())
                return f"{len(programs)} (Win32_Product)"
            return "Unknown"
        except Exception:
            return "Unknown"

    def get_shell(self):
        """Get current shell."""
        shell = os.getenv('SHELL', os.getenv('ComSpec', 'Unknown'))
        if shell != 'Unknown':
            return Path(shell).name
        return shell

    def get_terminal(self):
        """Get terminal information."""
        # Windows Terminal detection
        if os.getenv('WT_SESSION'):
            return "Windows Terminal"
        elif os.getenv('ConEmuPID'):
            return "ConEmu"
        elif 'powershell' in os.getenv('PSModulePath', '').lower():
            return "PowerShell"
        elif os.getenv('TERM_PROGRAM'):
            return os.getenv('TERM_PROGRAM')
        else:
            return "Windows Console"

    def get_cpu(self):
        """Get CPU information."""
        try:
            if self._wmi_conn:
                for processor in self._wmi_conn.Win32_Processor():
                    name = processor.Name.strip()
                    cores = processor.NumberOfCores
                    threads = processor.NumberOfLogicalProcessors
                    return f"{name} ({cores}C/{threads}T)"
            
            # Fallback
            return platform.processor()
        except Exception:
            return platform.processor()

    def get_memory(self):
        """Get memory information."""
        try:
            memory = psutil.virtual_memory()
            total_gb = memory.total / (1024**3)
            used_gb = memory.used / (1024**3)
            percentage = memory.percent
            return f"{used_gb:.1f}GB / {total_gb:.1f}GB ({percentage:.1f}%)"
        except Exception:
            return "Unknown"

    def get_gpu(self):
        """Get GPU information."""
        try:
            if self._wmi_conn:
                gpus = []
                for gpu in self._wmi_conn.Win32_VideoController():
                    if gpu.Name and "Microsoft" not in gpu.Name:
                        gpus.append(gpu.Name.strip())
                return gpus if gpus else ["Unknown"]
            return ["Unknown"]
        except Exception:
            return ["Unknown"]

    def get_disk_usage(self):
        """Get disk usage for the system drive."""
        try:
            # Get C: drive usage by default
            usage = psutil.disk_usage('C:')
            total_gb = usage.total / (1024**3)
            used_gb = usage.used / (1024**3)
            percentage = (usage.used / usage.total) * 100
            return f"{used_gb:.1f}GB / {total_gb:.1f}GB ({percentage:.1f}%)"
        except Exception:
            return "Unknown"

    def get_network_info(self):
        """Get network interface information."""
        try:
            interfaces = []
            for interface, addresses in psutil.net_if_addrs().items():
                if interface.startswith('Loopback') or 'Loopback' in interface:
                    continue
                for address in addresses:
                    if address.family == socket.AF_INET and not address.address.startswith('169.254'):
                        interfaces.append(f"{interface}: {address.address}")
            return interfaces[:3]  # Limit to first 3 interfaces
        except Exception:
            return ["Unknown"]

    def get_colors(self):
        """Get terminal color support information."""
        # Simple color detection - could be enhanced
        if os.getenv('COLORTERM') in ['truecolor', '24bit']:
            return "24-bit"
        elif os.getenv('TERM', '').endswith('256color'):
            return "256-color"
        else:
            return "8-color"
