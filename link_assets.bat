@echo off

setlocal enabledelayedexpansion

set src_dir=D:\Work\ExternalAssets\Peek\Content\
set dst_dir=D:\Work\MKGA\Content\

:: remove existing soft links
echo removing existing soft links...
for /d %%i in (%dst_dir%\*) do (
    :: is it a soft link
    if exist "%%i\*" (
        :: if /J Junction
        fsutil reparsepoint query "%%i" >nul 2>&1
        if not errorlevel 1 (
            rd "%%i"
            echo Removed soft link: %%i
        )
    )
)

:: check src.txt
if not exist src.txt (
    echo src.txt file does not exist!
    exit /b
)

:: read src.txt for dir name
for /f "delims=" %%i in (src.txt) do (
    set src_folder=!src_dir!%%i
    set dst_link=!dst_dir!%%i
    
    :: check src folder
    if exist "!src_folder!" (
        :: make soft link
        mklink /J "!dst_link!" "!src_folder!"
        echo Successfully make soft link: !dst_link! -> !src_folder!
    ) else (
        echo Source directory does not exist: !src_folder!
    )
)

echo Done.
pause