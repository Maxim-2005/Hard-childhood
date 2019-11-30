@echo off
chcp 1251 >nul
title Компиляция и запуск Java кода
mode con cols=64 lines=24
color 0a

echo %TIME% - Compilation
"C:\Program Files\Java\jdk-13.0.1\bin\javac.exe" Tetris.java

echo %TIME% - Start
"C:\Program Files\Java\jdk-13.0.1\bin\java.exe" Tetris
pause >nul