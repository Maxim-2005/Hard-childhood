@echo off
chcp 1251
title �����������
cls
:1
set /p NUM=������� ���������:
set /a NUM=%NUM%
echo �����: %NUM%
pause>nul
goto 1
