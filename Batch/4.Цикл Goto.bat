@echo off
chcp 1251
color 0a
cls
:1
<nul set /p =�
set /a X=%X%+1
if %X%==120 (pause>nul) else (goto 1)
                                