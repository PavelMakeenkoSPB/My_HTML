@echo off
@chcp 866
REM ����� ����᪠ � �ࠢ��� �����������
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

cls

:menu
echo _/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\
echo ===========================================================
echo *** [ 1 ] --  ������� 䠩�� � ����� system.32           ---
echo ===========================================================
echo *** [ 2 ] --  ��ᬮ���� ᮤ�ন��� ����� � �⨬ 䠩��� ---
echo ===========================================================
echo *** [ 3 ] --  ������� �������� ����� ��� ��ᬮ��      ---
echo ===========================================================
echo *** [ 4 ] --  (='.'=)          ���            (=-.-=) ---
echo ===========================================================

REM ���� ������
echo _______________________________ 
set /p inserted="������ ���� ��襣� �롮�: "
echo ******************************* 

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
	GOTO system32
) ELSE IF %choise%==2 (
	GOTO batFileDir
) ELSE IF %choise%==3 (
	GOTO yourDir
) ELSE IF %choise%==4 (
	GOTO end
) ELSE GOTO error

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
echo ___________________________________________________________
set /p yourDirictory="������ ���� � �������� �����, ���ਬ��: C:\Windows\ ===> "
IF EXIST "%yourDirictory%" (
	cd %yourDirictory%
	dir
	GOTO end
) ELSE (
	echo �� �������, ������ ���� � �������饩 �����
	GOTO yourDir)

REM ����饭�� �� �訡��
:error
echo ___________________________________________________________
echo ������ ����� �� ���४��. ��室 �� �ணࠬ�� � �訡���
pause
EXIT /b 128

REM �����襭�� ࠡ���
:end
echo *******************************
echo * �ᥬ ᯠᨡ�, �� ᢮�����! *
echo *******************************
pause
EXIT /b 0
echo on 

