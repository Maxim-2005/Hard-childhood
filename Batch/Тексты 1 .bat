echo off
chcp 1251 >nul
color 0a
title Тексты
cls
:1
set /p S=Введите слово: 
echo:
echo Первая буква
echo %S:~0,1%
pause >nul

echo:
echo Три последние буквы
echo %S:~-3%
pause >nul

echo:
echo Все слово кроме первых двух букв
echo %S:~2%
pause >nul

echo:
echo Три буквы начинае с третьей
echo %S:~2,3%
pause >nul

echo:
echo Удаление части строки
echo %S:бар=%
pause >nul

echo:
echo Замена части строки
echo %S:бар=-_- заменено -_-%
pause >nul
goto 1