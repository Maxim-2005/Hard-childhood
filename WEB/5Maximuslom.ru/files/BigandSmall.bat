echo off
chcp 1251
title ������ ������
cls
:start
set /a number=%random% %%1000 +1
:1
set /p num=������� �����: 
if %number% LSS %num% (echo ������)
:2
if %number% GTR %num% (echo ������) else goto 3
:3
if %number%==%num% (echo �� ������� ����� & echo %number% & goto start) else goto 1
cls
pause >nul



