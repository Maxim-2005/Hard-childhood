echo off
chcp 1251 >nul
color 0a
title ������
cls
:1
set /p S=������� �����: 

echo:
echo %S:~0,3%
pause >nul

echo:
echo %S:~3,4%
pause >nul

goto 1