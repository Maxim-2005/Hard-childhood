@echo off
chcp 1251
color 0a
title ����� � �����
cls
:1
echo:
echo Dir - ���������� �������
pause >nul
Dir
echo:
 
echo:
echo MD - ������� �������
pause >nul
Md "�����"
echo:
 
echo:
echo - ������� ����
pause >nul 
Copy nul "����� ����.txt"
echo:
 
echo:
echo Copy - ���������� ����
pause >nul
Copy "����� ����.txt" "����� ���� 2 .txt"
echo:
 
echo:
echo Tree - ����� �����
pause >nul
tree
echo:
 
echo:
echo Dir
pause >nul
Dir
echo:
 
echo:
echo Ren - �������������� �����
pause >nul
Ren "�����" "����� ���������������"
echo:
 
echo:
echo Ren - �������������� �����
pause >nul
Ren "����� ���� 2 .txt" "����� ���� 2 .html"
echo:
 
echo:
echo Move - ����������� ����
pause >nul
Move "����� ���� 2 .html" "����� ���������������\����� ���� 2 .html"
echo:
 
echo:
echo Cd - ������� � ����� 
pause >nul
Cd "����� ���������������"
echo:
 
echo:
echo Del - ������� ����
pause >nul
Del "����� ���� 2 .html"
echo:
 
echo:
echo Cd - ������� � �������� �����
pause >nul
Cd ..
echo:
 
echo:
echo Rd - ������� ������� � �������
pause >nul
Rd /s /q "����� ���������������"
echo:

echo:
echo Del - ������� ����
pause >nul
Del "����� ����.txt"
echo:
goto 1