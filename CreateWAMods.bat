@echo off
setlocal EnableExtensions
cd /d "%~dp0"

rem Recreate release-track mods named in config\config.YAML:
rem   base_game, gameplay_release, gameplay_dev, ui_only_release
rem Steam must be on the public WARNO branch.

call :LoadConfig
if errorlevel 1 goto :Failed
call :ReadConfigValue warno_mods WARNO_MODS
if errorlevel 1 goto :Failed
call :ReadConfigValue base_game MOD_BASE
if errorlevel 1 goto :Failed
call :ReadConfigValue gameplay_release MOD_RELEASE
if errorlevel 1 goto :Failed
call :ReadConfigValue gameplay_dev MOD_DEV
if errorlevel 1 goto :Failed
call :ReadConfigValue ui_only_release MOD_UI
if errorlevel 1 goto :Failed

if not exist "%WARNO_MODS%\Utils\Scripts\CreateNewMod.py" (
    echo warno_mods does not look like a WARNO Mods folder:
    echo   "%WARNO_MODS%"
    goto :Failed
)

call :ReadBranch
if errorlevel 1 goto :Failed
set "ABORT=0"
if "%IS_VIP%"=="1" (
    echo This WARNO install is on the full_vip beta.
    echo Switch Steam to the public branch, let the game update, then run CreateWAMods.bat.
    set "ABORT=1"
)
if "%ABORT%"=="1" goto :Failed

echo Release branch detected.
echo Using Mods folder:
echo   "%WARNO_MODS%"
echo Deleting and recreating:
echo   "%MOD_BASE%"
echo   "%MOD_RELEASE%"
echo   "%MOD_DEV%"
echo   "%MOD_UI%"
echo.

call :RecreateMod "%MOD_BASE%"
if errorlevel 1 goto :Failed
call :RecreateMod "%MOD_RELEASE%"
if errorlevel 1 goto :Failed
call :RecreateMod "%MOD_DEV%"
if errorlevel 1 goto :Failed
call :RecreateMod "%MOD_UI%"
if errorlevel 1 goto :Failed

echo.
echo Release mods recreated.
pause
exit /b 0

:Failed
echo.
echo Stopped.
pause
exit /b 1

:LoadConfig
set "CONFIG=%~dp0config\config.YAML"
if not exist "%CONFIG%" set "CONFIG=%~dp0config\config.yaml"
if not exist "%CONFIG%" set "CONFIG=%~dp0config\config.yml"
if not exist "%CONFIG%" (
    echo Could not find config\config.YAML next to this script.
    echo Copy config\config.template.YAML to config\config.YAML and set directories.warno_mods.
    exit /b 1
)
exit /b 0

:ReadConfigValue
set "CFGKEY=%~1"
set "CFGDEST=%~2"
set "CFGVAL="
for /f "usebackq delims=" %%P in (`findstr /R /C:"^[ ]*%CFGKEY%[ ]*:" "%CONFIG%" ^| python3 -c "import sys; line=sys.stdin.readline(); v=line.split(':',1)[1].strip().strip(chr(34)+chr(39)); print(v)"`) do (
    if not defined CFGVAL set "CFGVAL=%%P"
)
if not defined CFGVAL (
    echo Missing %CFGKEY% in "%CONFIG%".
    exit /b 1
)
set "%CFGDEST%=%CFGVAL%"
exit /b 0

:ReadBranch
set "MANIFEST=%WARNO_MODS%\..\..\..\appmanifest_1611600.acf"
if not exist "%MANIFEST%" (
    echo Could not find the Steam app manifest:
    echo   "%MANIFEST%"
    echo Refusing to delete mods without knowing whether this install is release or VIP.
    exit /b 1
)
set "IS_VIP=0"
findstr /C:"BetaKey" "%MANIFEST%" | findstr /C:"full_vip" >nul
if not errorlevel 1 set "IS_VIP=1"
exit /b 0

:RecreateMod
set "MODNAME=%~1"
set "MODPATH=%WARNO_MODS%\%MODNAME%"
echo Recreating "%MODNAME%"...
if exist "%MODPATH%" echo   Deleting existing "%MODNAME%"...
if exist "%MODPATH%" rmdir /s /q "%MODPATH%"
if exist "%MODPATH%" echo   Failed to delete "%MODNAME%". Close WARNO and anything else using that folder, then run this again.
if exist "%MODPATH%" exit /b 1
pushd "%WARNO_MODS%"
python3 Utils\Scripts\CreateNewMod.py "%MODNAME%"
popd
if not exist "%MODPATH%\GameData\" echo   Failed to create "%MODNAME%".
if not exist "%MODPATH%\GameData\" exit /b 1
echo   Created "%MODNAME%".
exit /b 0
