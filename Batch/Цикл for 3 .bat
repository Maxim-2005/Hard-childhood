echo off
chcp 1251
title ���� for
color 0a
cls
:1
for /L %%N in (5,-1,1) do (
echo %%N
timeout 1 >nul
cls)
echo ���
pause >nul
goto 1
