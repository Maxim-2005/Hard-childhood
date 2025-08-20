from random import randint
import pyautogui as pg
import pyperclip as pc
import requests
from bs4 import BeautifulSoup
import pyperclip
import time

# Разметка кнопок
pnt_exit = [100, 1360]              # Выйти
pnt_send_exit = [100, 1260]         # Отправить и выйты
pnt_actv = [2000, 1000]             # Окно браузера
pnt_blue_box = [1350, 700]          # Нет заданий
pnt_task_verifer = [1170, 295]      # Проверка доступности задания
pnt_task_check = [1015, 300]        # Проверка задания
pnt_task_start = [1500, 370]        # Запуск задания
pnt_specifier_first = [80, 170]     # Координаты 1 карточки
pnt_specifier_middle = [80, 250]    # Коориднаты 2-9 карточек
pnt_specifier_last = [70, 310]      # Координаты 10 карточки

url = "https://yang.yandex-team.ru/task/82961255/"
btn_key = "0"
img_type = ""
pg.PAUSE = 0.2
pg.FAILSAFE = True

# Парсер по html тэгам
def parse_and_copy(url):
    try:
        # Получаем HTML страницы
        response = requests.get(url)
        response.raise_for_status()  # Проверяем успешность запроса
    
        # Парсим HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ищем нужный div по классу
        target_div = soup.find('div', class_='label_3kPe4')

        if target_div:
            # Извлекаем текст
            text = target_div.get_text(strip=True)
            print(f"Найден текст: {text}")
            
            # Копируем в буфер обмена
            pyperclip.copy(text)
            print("Текст скопирован в буфер обмена!")
            return text
        else:
            print("Div с классом 'label_3kPe4' не найден")
            return None

    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


# Парсер текста по координатам
def parcer_text(cord):
    pg.moveTo(cord[0], cord[1])
    pg.tripleClick()
    pg.hotkey('ctrl', 'c')
    # Проверка пробелов по краям
    text = pc.paste().strip()
    text = text[:16]
    print(text)
    return text

# Выбор ответа
def answer(pnt_specifier):
    img_type = parcer_text(pnt_specifier)
    if img_type == "На фото должен б":
        pg.hotkey("3")
    else:
        pg.hotkey("0")

# Главный цикл
while True:
    # Выбор окна браузера
    pg.moveTo(pnt_actv[0], pnt_actv[1])
    pg.click()
    pg.hotkey("F5") # Обновление странички
    time.sleep(2 + (randint(0, 100) / 100)) # Выдерживаем паузу
    # Проверка наличия заданий на столе
    if parcer_text(pnt_task_check) != "Задания закончил":
        # Запуск задания
        if parcer_text(pnt_task_check) == "Проверка фотогра":
            pg.moveTo(pnt_task_start[0], pnt_task_start[1])
            pg.click()
            pg.moveTo(pnt_actv[0], pnt_actv[1])
            time.sleep(3) # Выдерживаем паузу
            # Проверка доступности задания
            if parcer_text(pnt_task_verifer) != "Это задание в ра":
                # Выполнение задания
                pg.moveTo(pnt_actv[0], pnt_actv[1])
                error_task = randint(0, 10)
                for i in range(10):
                    #if i == 0:
                    #    answer(pnt_specifier_first)
                    #elif i == 9:
                    #    answer(pnt_specifier_last)
                    #else:
                    #    answer(pnt_specifier_middle)
                    if i == error_task:
                        key = str(randint(3, 7))
                        pg.hotkey(key)
                    else:
                        pg.hotkey("0")
                    pg.hotkey("Down")
                    time.sleep(1 + (randint(0, 100) / 100))
                # Сдача задания
                pg.moveTo(pnt_exit[0], pnt_exit[1])
                pg.click()
                time.sleep(1)
                pg.moveTo(pnt_send_exit[0], pnt_send_exit[1])
                pg.click()
                time.sleep(2)
    
"На фото должны быть четко и полностью видны наклейка на посылке с/без штрихкода или чек от посылки."