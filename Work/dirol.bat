
echo off
cls
echo =================================
echo ==  1 ==== system.32 ============
echo =================================
echo === 2 === what about my files? ==
echo =================================
echo === 3 ====     quit      ========
echo =================================
echo ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 

set wind=C:\Windows\System32
set current=C:\pavel\My_HTML\Work

cd %wind% 
cd %current%


set /p choise="insert number: "
echo You have inserted: %choise%

IF %choise%==1 GOTO t1

IF %choise%==2 GOTO t2

IF NOT %choise%==1 GOTO t3
IF NOT %choise%==2 GOTO t3

:t1
cd %wind% 
dir


:t2
cd %curren% 
dir


:t3
echo Bu!


pause
echo on 


