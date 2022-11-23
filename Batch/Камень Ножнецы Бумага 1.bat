@echo off
chcp 1251
cls
title Камень Ножнецы Бумага
:1
set /a RND=1+3*%random%/32767
if %rnd%==1 (echo Камень)
if %rnd%==2 (echo ножницы)
if %rnd%==3 (echo бумага)
pause
cls
goto 1



