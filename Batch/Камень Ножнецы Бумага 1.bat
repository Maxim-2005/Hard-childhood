@echo off
chcp 1251
cls
title ������ ������� ������
:1
set /a RND=1+3*%random%/32767
if %rnd%==1 (echo ������)
if %rnd%==2 (echo �������)
if %rnd%==3 (echo ������)
pause
cls
goto 1



