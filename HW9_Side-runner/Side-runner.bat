@echo off
@chcp 866

REM ����� ����᪠ � �ࠢ��� �����������
REM if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

TITLE Side-runner
cls
color F0
set PATH=%PATH%;C:\temp\driver
set current=/d "%~dp0"
cd %current%


:mainMenu

echo ����������������������� ������� ���� ����������������������
echo ���������������������������������������������������������ͻ
echo �  [ 1 ] --  ��⠭���� �ᥣ� ����室�����              --�
echo �=========================================================�
echo �  [ 2 ] --  ����� .side �஥�⮢                     --�
echo �=========================================================�
echo �  [ 3 ] --  ��३� � ����� � �������� ���᮫�       --�
echo �=========================================================�
echo �  [ 4 ] --  (='.'=)     ���     (=-.-=)             --�
echo ���������������������������������������������������������ͼ

GOTO insert



:insert
REM ���� ������
echo _______________________ 
set /p inserted="������ ���� ०���: "

REM ��᢮���� ����񭭮�� ���祭�� ��ଥ����, ����� ����� ���� ⮫쪮 �᫮�
set /a choise=%inserted%

REM �஢�ઠ ������ �� �ਭ���������� � �᫠�. �᫨ ��᢮��� �� �᫮, ��६����� ����� ���祭��  0
IF %choise% leq 0 (
	GOTO error
)ELSE (
	GOTO action
)

REM �᫮��� ࢡ��� �ணࠬ��
:action
IF %choise%==1 (
	GOTO setupMenu
) ELSE IF %choise%==2 (
	GOTO sideMenu
) ELSE IF %choise%==3 (
	GOTO yourDir
) ELSE IF %choise%==4 (
	GOTO end
) ELSE GOTO mainMenu

REM ��ᬮ�� system32
:system32
set wind=C:\Windows\System32
cd %wind% 
dir
GOTO end

REM ��ᬮ�� ⥪�饩 ����� � bat 䠩���
:batFileDir
set current=/d "%~dp0"
cd %current% 
dir
GOTO end

REM ��ᬮ�� 㪠������ ����� 
:yourDir
echo __________________________________________________________________________________
set /p yourDirictory="������ ���� � �������� �����, ���ਬ��: C:\Windows\, ��� 4 ��� �뢮�� ���� ===> "
IF EXIST "%yourDirictory%" (
	cd %yourDirictory%
	dir
	GOTO cmdLine
) ELSE IF %yourDirictory%==4 (
	GOTO mainMenu
) ELSE (
	echo �� 㪠������� ����� ��祣� �� ������� :(
	GOTO yourDir)

REM ����饭�� �� �訡�� � ��室
:error
echo ___________________________________________________________
echo ������ ����� �����४��. ��室 �� �ணࠬ�� � �訡���
pause
EXIT /b 128

REM ���� �롮� ��⠭���� � ����஥�
:setupMenu
echo ���������������������� ���� ��������� ���������������������
echo ���������������������������������������������������������ͻ
echo � [ 1 ] --  ��⠭����� Node.js                        --�
echo �=========================================================�
echo � [ 2 ] --  ��⠭����� Side-runner                    --�
echo �=========================================================�
echo � [ 3 ] --  ��������� webdrivers                     --�
echo �=========================================================�
echo � [ 4 ] --  (='.'=)     ���     (=-.-=)             --�
echo ���������������������������������������������������������ͼ

GOTO setupInsert

REM ���� � �஢�ઠ ������ ����짮��⥫�
:setupInsert
echo _______________________ 
set /p inserted="������ ���� ��⠭��騪�: "

REM ��᢮���� ����񭭮�� ���祭�� ��ଥ����, ����� ����� ���� ⮫쪮 �᫮�
set /a choise=%inserted%

REM �஢�ઠ ������ �� �ਭ���������� � �᫠�. �᫨ ��᢮��� �� �᫮, ��६����� ����� ���祭��  0
IF %choise% leq 0 (
	GOTO setupMenu
)ELSE (
	GOTO setupAction
)

REM �롮� �㭪樨� ��⠭��騪�
:setupAction
IF %choise%==1 (
	GOTO nodeSetup
) ELSE IF %choise%==2 (
	GOTO sideSetup
) ELSE IF %choise%==3 (
	GOTO webdriverSetup
) ELSE IF %choise%==4 (
	GOTO mainMenu
) ELSE GOTO setupMenu

REM ����� ��⠭���� Node.js
:nodeSetup
node-v18.16.0-x64.msi
GOTO setupMenu

REM ����� ��⠭���� selenium-side-runner
:sideSetup
npm install -g selenium-side-runner@3.17.0
REM npm install -g @3.17.0
GOTO setupMenu

REM ���稢���� �ࠩ��஢ � ����஢���� ᪠祭��� ࠭�� � �����, 㪠������ � PATH
:webdriverSetup
npm install -g chromedriver
npm install -g edgedriver
npm install -g geckodriver
npm install -g iedriver

set DriverDir=C:\temp\driver
IF NOT EXIST "%DriverDir%" mkdir C:\temp\driver
REM set PATH=%PATH%;C:\temp\driver
copy driver C:\temp\driver 
GOTO setupMenu


REM ���� �롮� ०���� ࠡ��� SIDE-RUNNER
:sideMenu
echo ������������������������ SIDE-RUNNER ����������������������
echo ���������������������������������������������������������ͻ
echo �   [ 1 ] --  �ᯮ�짮���� Chrome                    --�
echo �=========================================================�
echo �   [ 2 ] --  �ᯮ�짮���� Firefox                   --�
echo �=========================================================�
echo �   [ 3 ] --  �ᯮ�짮���� Edge                      --�
echo �=========================================================�
echo �   [ 4 ] --  �ᯮ�짮���� IE                        --�
echo �=========================================================�
echo �   [ 5 ] --  ��� � ������� ����                   --�
echo ���������������������������������������������������������ͼ

GOTO sideInsert

:sideInsert
REM ���� ������
echo _______________________ 
set /p inserted="������ ���� ��㧥�: "

REM ��᢮���� ����񭭮�� ���祭�� ��ଥ����, ����� ����� ���� ⮫쪮 �᫮�
set /a choise=%inserted%

REM �஢�ઠ ������ �� �ਭ���������� � �᫠�. �᫨ ��᢮��� �� �᫮, ��६����� ����� ���祭��  0
IF %choise% leq 0 (
	GOTO sideMenu
)ELSE (
	GOTO side-RunnerAction
)


:side-RunnerAction
IF %choise%==1 (
	GOTO sideChrome
) ELSE IF %choise%==2 (
	GOTO sideFirefox
) ELSE IF %choise%==3 (
	GOTO sideEdge
) ELSE IF %choise%==4 (
	GOTO sideIE
) ELSE IF %choise%==5 (
	GOTO mainMenu
)ELSE GOTO sideMenu



:sideChrome
set /p sidePath="㪠��� ���� �� 䠩�� .side, ���ਬ�� C:\temp\1.side ===>  "
npm selenium-side-runner -c "browserName=chrome" %sidePath%
GOTO sideMenu

:sideFirefox
set /p sidePath="㪠��� ���� �� 䠩�� .side, ���ਬ�� C:\temp\1.side ===>  "
npm selenium-side-runner -c "browserName=firefox" %sidePath%
GOTO sideMenu

:sideEdge
set /p sidePath="㪠��� ���� �� 䠩�� .side, ���ਬ�� C:\temp\1.side ===>  "
npm selenium-side-runner -c "browserName=edge" %sidePath%
GOTO sideMenu

:sideIE
set p/ sidePath="㪠��� ���� �� 䠩�� .side, ���ਬ�� C:\temp\1.side ===>  "
npm selenium-side-runner -c "browserName='internet explorer'" %sidePath%
GOTO sideMenu

:cmdLine
cmd


REM �����襭�� ࠡ���
:end
echo �������������������������������
echo � �ᥬ ᯠᨡ�, �� ᢮�����! �
echo �������������������������������
pause
EXIT /b 0
echo on 


