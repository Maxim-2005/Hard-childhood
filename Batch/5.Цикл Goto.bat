@echo off
chcp 1251
cls
:1
<nul set /p =Æ
set /a X1=%X1%+1
if %X1%==145 (goto 2) else (goto 1)
:2
set /a X2=%X2%+1
echo.
if %X2%==37 (goto 3) else (set /a X1=0 & goto 1)
:3
pause>nul                             