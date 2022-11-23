echo off
chcp 1251
title Больше меньше
cls
:start
set /a number=%random% %%1000 +1
:1
set /p num=Введите число: 
if %number% LSS %num% (echo Меньше)
:2
if %number% GTR %num% (echo Больше) else goto 3
:3
if %number%==%num% (echo Вы угадали число & echo %number% & goto start) else goto 1
cls
pause >nul



