@echo off
chcp 1251
cls
title Камень Ножнецы Бумага
:1
echo: 000                 ##########     !!!!!!!!!!!!!!!!
echo: 000                ############    !!!!!!!!!!!!!!!!
echo:    \\\\\\\\\\\\   ##############   !!!!!!!!!!!!!!!!
echo:    ////////////  ################  !!!!!!!!!!!!!!!!
echo: 000               ##############   !!!!!!!!!!!!!!!!
echo: 000                ############    !!!!!!!!!!!!!!!!
choice /c 123 /n /m "Выберите 1-Камень 2-Ножнецы или 3-Бумагу: "
set knb=%errorlevel%
cls
if %knb%==1 (echo Вы: Камень)
if %knb%==2 (echo Вы: ножницы)
if %knb%==3 (echo Вы: бумага)
set /a RND=1+3*%random%/32767
if %rnd%==1 (echo ИИ: Камень)
if %rnd%==2 (echo ИИ: ножницы)
if %rnd%==3 (echo ИИ: бумага)
set /a GAME=%GAME%+1
::Ничья
if %rnd%==%knb% (echo Ничья & set /a DRAW=%DRAW%+1)
::Победы
if %knb%==1 (if %rnd%==2 (echo Вы победили & set /a WIN=%WIN%+1))
if %knb%==2 (if %rnd%==3 (echo Вы победили & set /a WIN=%WIN%+1))
if %knb%==3 (if %rnd%==1 (echo Вы победили & set /a WIN=%WIN%+1))
::Проигршы
if %knb%==1 (if %rnd%==3 (echo Вы проиграли & set /a LOSE=%LOSE%+1))
if %knb%==2 (if %rnd%==1 (echo Вы проиграли & set /a LOSE=%LOSE%+1))
if %knb%==3 (if %rnd%==2 (echo Вы проиграли & set /a LOSE=%LOSE%+1))

echo Всего игр: %GAME% Ничьих: %DRAW% Побед: %WIN% Проигроши: %LOSE%
goto 1



