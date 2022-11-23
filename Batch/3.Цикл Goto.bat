@echo off
chcp 1251
color 0a
cls
:1
echo Æ
set /a X=%X%+1
if %X%==10 (pause>nul) else (goto 1)                                     