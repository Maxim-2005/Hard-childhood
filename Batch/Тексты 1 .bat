echo off
chcp 1251 >nul
color 0a
title ������
cls
:1
set /p S=������� �����: 
echo:
echo ������ �����
echo %S:~0,1%
pause >nul

echo:
echo ��� ��������� �����
echo %S:~-3%
pause >nul

echo:
echo ��� ����� ����� ������ ���� ����
echo %S:~2%
pause >nul

echo:
echo ��� ����� ������� � �������
echo %S:~2,3%
pause >nul

echo:
echo �������� ����� ������
echo %S:���=%
pause >nul

echo:
echo ������ ����� ������
echo %S:���=-_- �������� -_-%
pause >nul
goto 1