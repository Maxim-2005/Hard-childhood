@echo off
chcp 1251
color 0a
cls
:1
set /p S=¬ведите размер треугольника: 
set /a S1=%S%-1
echo:
for /L %%N in (1,1,%S%) do <nul set /p = 


for /L %%N in (3,1,%S%) do (
	echo:
	<nul set /p = 
	for /L %%N in (%S1%,-1,%%N) do <nul set /p =. 
	<nul set /p =
	)
echo:
echo 
pause >nul
cls
goto 1