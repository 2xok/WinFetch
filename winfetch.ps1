# WinFetch - PowerShell launcher script
# This script allows you to run WinFetch from anywhere

param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Arguments
)

# Get the directory where this script is located
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Try to find Python executable
$PythonExe = $null

# Check if python is in PATH
try {
    $null = Get-Command python -ErrorAction Stop
    $PythonExe = "python"
    Write-Verbose "Found Python in PATH"
} catch {
    # Check common Python installation paths
    $PythonPaths = @(
        "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe",
        "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe",
        "$env:LOCALAPPDATA\Programs\Python\Python310\python.exe",
        "C:\Python312\python.exe",
        "C:\Python311\python.exe",
        "C:\Python310\python.exe"
    )
    
    foreach ($Path in $PythonPaths) {
        if (Test-Path $Path) {
            $PythonExe = $Path
            Write-Verbose "Found Python at: $Path"
            break
        }
    }
}

if (-not $PythonExe) {
    Write-Error "Python not found!"
    Write-Host "Please ensure Python 3.7+ is installed and either:" -ForegroundColor Yellow
    Write-Host "1. Add Python to your PATH, or" -ForegroundColor Yellow
    Write-Host "2. Install Python using: winget install Python.Python.3.12" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "You can also run WinFetch directly with:" -ForegroundColor Cyan
    Write-Host "python `"$ScriptDir\main.py`" $($Arguments -join ' ')" -ForegroundColor Cyan
    exit 1
}

# Run WinFetch with all passed arguments
$MainScript = Join-Path $ScriptDir "main.py"
& $PythonExe $MainScript @Arguments
