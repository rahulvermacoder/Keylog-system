@echo off
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Downloading and installing now...
     
    REM Set Python installer URL (Update version if needed)
    set "PYTHON_INSTALLER=https://www.python.org/ftp/python/3.13.1/python-3.13.1.exe"
    
    REM Download Python installer using PowerShell
    powershell -Command "Invoke-WebRequest -Uri %PYTHON_INSTALLER% -OutFile python-installer.exe"    
    REM Install Python silently
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    
    REM Delete the installer after installation
    del python-installer.exe

    echo Python installation completed. Please restart your computer and run this app again.
    pause
    exit /b
) ELSE (
    echo Python is installed. Running your application...
    
    REM Start the application
    start "" "%USERPROFILE%\Downloads\dist\main\main.exe""
)
