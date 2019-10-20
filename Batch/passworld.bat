@echo off
chcp 1251
cls
color 0a
title Пароль
:1
set /p Pass=Пароль:
if %Pass%==123456 (goto 2) else (echo Пароль неверный && goto 1)
:2
echo Пароль верный
pause >nul
