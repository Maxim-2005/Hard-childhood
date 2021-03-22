#RATORI-game
__author__ = "Maxim "
from modules.Main import Main
from pyautogui import *

current_version = 1 #Запрос версии с интернета

if __name__ == '__main__':
    window_name = 'update'
    window_text = 'Вышла новая версия игры RaToRi'
    main = Main()
    local_version = main.local_version
    if local_version < current_version:
        print(window_text)
        alert(window_text, window_name, button='OK')
    else:
        main.game_start()