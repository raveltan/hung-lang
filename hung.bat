@echo off
:: Check for Python Installation
py --version 2>NUL
if errorlevel 1 goto errorNoPython

:: Reaching here means Python is installed.
@echo on
py bin\main.py

:: Once done, exit the batch file -- skips executing the errorNoPython section
goto:eof

:errorNoPython
echo     __  __            ______
echo    / / / /_  ______  / ____/
echo   / /_/ / / / / __ \/ / __ 
echo  / __  / /_/ / / / / /_/ /  
echo /_/ /_/\__,_/_/ /_/\____/  
echo ........................
echo Unable to run HunG,
echo Error^: Python3 not installed
echo Please install Python3 to run HunG!
pause