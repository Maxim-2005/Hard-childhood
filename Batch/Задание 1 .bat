@echo off
chcp 1251
color 0a
cls
:1
set /p S=¬ведите число: 
for /L %%N in (1,1,%S%) do <nul set /p =
pause >nul
cls
goto 1