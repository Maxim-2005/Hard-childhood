@echo off
chcp 1251
title ����������
mode con cols=80 lines=20
color 0a

echo ���� ����� ����������� ������� ����� ��������

echo:
pyinstaller --onefile --icon="view\img\icon.ico" -w MaxHUB.py
echo:

copy /Y "dist\MaxHUB.exe" MaxHUB.exe >nul
RD /S /Q "dist"
RD /S /Q "build"
del /Q "MaxHUB.spec"

echo ���������� ���������

echo ���� ������� �� ������� ����� data ����� JSON � SQL
echo � ���������� ���� �������� ��� ������ �����, ������

pause >nul