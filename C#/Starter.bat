@echo off
chcp 1251 >nul
title Компиляция и запуск Java кода
mode con cols=48 lines=24
color 0a

echo %TIME% - Compilation
"C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe" "Hello World.cs"