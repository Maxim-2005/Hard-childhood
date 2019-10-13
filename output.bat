@echo off
chcp 1251
title Выводитель
cls
:1
set /p TXT=Введите текст 
echo Вы написали %TXT%
pause>nul
cls
goto 1
