@echo off
chcp 1251
title Калькулятор
cls
:1
set /p NUM=Введите выражения:
set /a NUM=%NUM%
echo Ответ: %NUM%
pause>nul
goto 1
