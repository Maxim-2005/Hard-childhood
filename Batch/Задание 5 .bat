@echo off
chcp 1251
color 0a
cls
:�����
cls
set /p S=������� ������ ���������: 
call :�����
call :�������
call :�����
echo:
call :�����
call :�������
call :�����
pause >nul
goto �����

:�����
for /L %%N in (1,1,%S%) do <nul set /p = 
echo: 
exit /b

:�������
for /L %%N in (3,1,%S%) do (
<nul set /p = 
for /L %%N in (3,1,%S%) do <nul set /p =. 
echo )
exit /b