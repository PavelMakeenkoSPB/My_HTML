set DriverDir=C:\temp\driver
IF NOT EXIST "%DriverDir%" mkdir C:\temp\driver
set PATH=%PATH%;C:\temp\driver
copy driver C:\temp\driver
pause