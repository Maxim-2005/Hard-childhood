::Программа отчистки папки Temp 03.02.2019
@echo off
title Clear Temp
del /Q /F /S %TEMP%\*
