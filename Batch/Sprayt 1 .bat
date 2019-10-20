echo off
chcp 1251
color 3d
title Sprayt
setlocal ENABLEdelayEdexpanSION
:1
set X=1
mode con cols=102 lines=60
FOR /F "usebackq delims=" %%i IN (Sprayt.txt) DO (
	echo.%%i
	set /a X=X+1
	if !X! gtr 57 (
		set X=1
		>nul pathping /h 1 /p 80 /q 1 /w 1 127.0.0.1
::pause >nul
		cls
		)
	)
goto 1