REM set DriverDir=C:\temp\driver
REM IF NOT EXIST "%DriverDir%" mkdir C:\temp\driver
REM set PATH=%PATH%;C:\temp\driver
REM copy driver C:\temp\driver
REM pause


REM npm install -g chromedriver
REM GOTO edgeDown
REM :edgeDown
REM npm install -g edgedriver
REM REM GOTO firefoxDown
REM :firefoxDown
REM npm install -g geckodriver
REM GOTO IEDown
REM :IEDown
REM npm install -g iedriver

set DriverDir=C:\temp\driver
set /p sidePath="укажите путь до файла .side, например C:\temp\1.side ===>  "
selenium-side-runner -c "browserName='internet explorer'" %sidePath%
pause