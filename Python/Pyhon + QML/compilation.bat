@echo off
chcp 1251
title ����������
mode con cols=80 lines=20
color 0a

echo:
pyinstaller --onefile -w main.py
echo:

copy /Y "dist\main.exe" main.exe >nul
RD /S /Q "dist"
RD /S /Q "build"
del /Q "main.spec"

echo ���������� ���������

pause >nul