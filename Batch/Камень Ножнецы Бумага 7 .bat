@echo off
chcp 1251
cls
title ������ ������� ������
:1
echo: 000                 ##########     !!!!!!!!!!!!!!!!
echo: 000                ############    !!!!!!!!!!!!!!!!
echo:    \\\\\\\\\\\\   ##############   !!!!!!!!!!!!!!!!
echo:    ////////////  ################  !!!!!!!!!!!!!!!!
echo: 000               ##############   !!!!!!!!!!!!!!!!
echo: 000                ############    !!!!!!!!!!!!!!!!
choice /c 123 /n /m "�������� 1-������ 2-������� ��� 3-������: "
set knb=%errorlevel%
cls
if %knb%==1 (echo ��: ������)
if %knb%==2 (echo ��: �������)
if %knb%==3 (echo ��: ������)
set /a RND=1+3*%random%/32767
if %rnd%==1 (echo ��: ������)
if %rnd%==2 (echo ��: �������)
if %rnd%==3 (echo ��: ������)
set /a GAME=%GAME%+1
::�����
if %rnd%==%knb% (echo ����� & set /a DRAW=%DRAW%+1)
::������
if %knb%==1 (if %rnd%==2 (echo �� �������� & set /a WIN=%WIN%+1))
if %knb%==2 (if %rnd%==3 (echo �� �������� & set /a WIN=%WIN%+1))
if %knb%==3 (if %rnd%==1 (echo �� �������� & set /a WIN=%WIN%+1))
::��������
if %knb%==1 (if %rnd%==3 (echo �� ��������� & set /a LOSE=%LOSE%+1))
if %knb%==2 (if %rnd%==1 (echo �� ��������� & set /a LOSE=%LOSE%+1))
if %knb%==3 (if %rnd%==2 (echo �� ��������� & set /a LOSE=%LOSE%+1))

echo ����� ���: %GAME% ������: %DRAW% �����: %WIN% ���������: %LOSE%
goto 1



