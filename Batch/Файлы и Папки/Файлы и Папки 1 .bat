@echo off
chcp 1251
color 0a
title Файлы и Папки
cls
:1
echo:
echo Dir - Посмотреть каталог
pause >nul
Dir
echo:
 
echo:
echo MD - Создать каталог
pause >nul
Md "Папка"
echo:
 
echo:
echo - Создать файл
pause >nul 
Copy nul "Новый файл.txt"
echo:
 
echo:
echo Copy - Копировать файл
pause >nul
Copy "Новый файл.txt" "Новый файл 2 .txt"
echo:
 
echo:
echo Tree - Древо папок
pause >nul
tree
echo:
 
echo:
echo Dir
pause >nul
Dir
echo:
 
echo:
echo Ren - Переиминование папки
pause >nul
Ren "Папка" "Папка переименованная"
echo:
 
echo:
echo Ren - Переиминование файлы
pause >nul
Ren "Новый файл 2 .txt" "Новый файл 2 .html"
echo:
 
echo:
echo Move - Переместить файл
pause >nul
Move "Новый файл 2 .html" "Папка переименованная\Новый файл 2 .html"
echo:
 
echo:
echo Cd - Переход в папку 
pause >nul
Cd "Папка переименованная"
echo:
 
echo:
echo Del - Удалить файл
pause >nul
Del "Новый файл 2 .html"
echo:
 
echo:
echo Cd - Возврат в корневую папку
pause >nul
Cd ..
echo:
 
echo:
echo Rd - Удаляем каталог с файлами
pause >nul
Rd /s /q "Папка переименованная"
echo:

echo:
echo Del - Удаляем файл
pause >nul
Del "Новый файл.txt"
echo:
goto 1