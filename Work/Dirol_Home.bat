@echo off

cls

set wind=C:\Windows\System32
set current=/d "%~dp0"

:begin
echo =================================
echo ==  1 ==== system.32 ============
echo =================================
echo === 2 === what about my files? ==
echo =================================
echo === 3 == choose your directory ==
echo =================================
echo === 4 ======== exit =============
echo =================================
echo ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 

set /p choise="insert number: "
echo You have inserted: %choise%

IF %choise%==1 (GOTO system32)

IF %choise%==2 (GOTO batFileDir) 

IF %choise%==3 GOTO yourDir

IF %choise%==4 GOTO end 



:system32
cd %wind% 
dir
GOTO begin

:batFileDir
cd %current% 
dir
GOTO begin

:yourDir
set /p yourDirictory="Type your Path, please, for example: C:\Windows\ ===> "
cd %yourDirictory%
dir
GOTO begin

:error
echo ERROR
pause
GOTO begin

:end
echo NOW WE GO AWAY
pause
EXIT /b 1

pause
echo on 

REM https://www.cyberforum.ru/cmd-bat/thread258321.html