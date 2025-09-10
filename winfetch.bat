@echo off
REM WinFetch - Easy launcher batch file
REM This batch file allows you to run WinFetch from anywhere

REM Get the directory where this batch file is located
set "SCRIPT_DIR=%~dp0"

REM Try to find Python in common locations
set "PYTHON_EXE="

REM Check if python is in PATH
python --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON_EXE=python"
    goto :run
)

REM Check common Python installation paths
if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe" (
    set "PYTHON_EXE=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe"
    goto :run
)

if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\python.exe" (
    set "PYTHON_EXE=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\python.exe"
    goto :run
)

if exist "C:\Python312\python.exe" (
    set "PYTHON_EXE=C:\Python312\python.exe"
    goto :run
)

if exist "C:\Python311\python.exe" (
    set "PYTHON_EXE=C:\Python311\python.exe"
    goto :run
)

REM If we get here, Python wasn't found
echo Error: Python not found!
echo Please ensure Python 3.7+ is installed and either:
echo 1. Add Python to your PATH, or
echo 2. Install Python using: winget install Python.Python.3.12
echo.
echo You can also run WinFetch directly with:
echo python "%SCRIPT_DIR%main.py" %*
pause
exit /b 1

:run
REM Run WinFetch with all passed arguments
"%PYTHON_EXE%" "%SCRIPT_DIR%main.py" %*

REM Pause so user can see the output when double-clicked
REM This detects if the batch was double-clicked vs run from command line
echo %CMDCMDLINE% | find /i "cmd /c" >nul && (
    echo.
    echo Press any key to close...
    pause >nul
)
