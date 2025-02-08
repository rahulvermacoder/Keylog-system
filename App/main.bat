@echo off

REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Downloading and installing now...
    
    REM Change folder permissions to allow SYSTEM access
    echo Changing folder permissions...
    icacls "%USERPROFILE%\Downloads\MyAPP\main" /remove Everyone
    icacls "%USERPROFILE%\Downloads\MyAPP\main" /grant SYSTEM:(OI^)(CI^)F
    
    set "PYTHON_INSTALLER=https://www.python.org/ftp/python/3.10.1/python-3.10.1.exe"
    echo Downloading Python installer...
    powershell -Command "Invoke-WebRequest -Uri %PYTHON_INSTALLER% -OutFile python-installer.exe"
    
    echo Installing Python...
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python-installer.exe
    echo Python installation completed. Checking for dependencies...
    
    REM Check if requirements.txt exists
    if exist requirements.txt (
        echo Installing dependencies from requirements.txt...
        pip install -r requirements.txt
    ) else (
        echo requirements.txt not found. Skipping dependency installation.
        exit /b
    )

    echo Running your application...
    
    REM Start the application
    start "" "%USERPROFILE%\Downloads\MyAPP\main\main.py"
    pause
    exit /b
) ELSE (
    echo Python is installed. Checking for dependencies...
    
    REM Change folder permissions to allow SYSTEM access
    echo Changing folder permissions...
    icacls "%USERPROFILE%\Downloads\MyAPP\main" /remove Everyone
    icacls "%USERPROFILE%\Downloads\MyAPP\main" /grant SYSTEM:(OI^)(CI^)F
    
    REM Check if requirements.txt exists
    if exist requirements.txt (
        echo Installing dependencies from requirements.txt...
        pip install -r requirements.txt
    ) else (
        echo requirements.txt not found. Skipping dependency installation.
        exit /b
    )

    echo Running your application...
    
    REM Start the application
    start "" "%USERPROFILE%\Downloads\MyAPP\main\main.py"
    pause
)