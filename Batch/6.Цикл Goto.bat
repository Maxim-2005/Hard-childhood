@echo off
chcp 1251
cls
color 0a
:4
set /a X1=0
set /a X2=0
set /p Y=Введите символ: 
cls
:1
<nul set /p =%Y%
set /a X1=%X1%+1
if %X1%==142 (goto 2) else (goto 1)
:2
set /a X2=%X2%+1
echo.
if %X2%==37 (goto 3) else (set /a X1=0 & goto 1) 
:3
goto 4
pause>nul
                            