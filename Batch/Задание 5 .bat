@echo off
chcp 1251
color 0a
cls
:Старт
cls
set /p S=Введите размер квадратов: 
call :Линия
call :Квадрат
call :Линия
echo:
call :Линия
call :Квадрат
call :Линия
pause >nul
goto Старт

:Линия
for /L %%N in (1,1,%S%) do <nul set /p = 
echo: 
exit /b

:Квадрат
for /L %%N in (3,1,%S%) do (
<nul set /p = 
for /L %%N in (3,1,%S%) do <nul set /p =. 
echo )
exit /b