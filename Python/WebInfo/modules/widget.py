import eel
import os
import webbrowser

def start():
    eel.init("web")

    # Прием сообщения с сайта
    @eel.expose
    def call_in_js(msg_in):
        if msg_in == 'quit':
            os.system("TASKKILL /F /IM Chrome.exe")
            quit()
        elif msg_in.isdigit():
            msg_out = int(msg_in)*int(msg_in)
        elif msg_in == 'calc':
            msg_out = 'Запуск калькулятора'
            os.system('D:/SOFT/Office/Калькулятор.exe')
        elif msg_in == 'paint':
            msg_out = 'Запуск паинта'
            os.system('%windir%/system32/mspaint.exe')
        elif msg_in == 'snippinghtool':
            msg_out = 'Запуск ножниц'
            os.system('%windir%/system32/SnippingTool.exe')
        elif msg_in == 'osu':
            msg_out = 'Запуск osu'
            os.system('D:\GAME\Osu\osu!.exe')
        elif msg_in == 'youtube':
            msg_out = 'Запуск ютуба'
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO')
        elif msg_in == 'discord':
            msg_out = 'Запуск дискорда'
            os.system('C:/Users/Администратор/AppData/Local/Discord/Update.exe --processStart Discord.exe')
        elif msg_in == 'weigartemp':
            msg_out = 'Очистка темпа'
            os.system('C:/Users/Администратор/Desktop/weigartemp.bat')
        else:
            msg_out = msg_in[::-1]
        call_in_python(msg_out)

    # Отправка сообщения на сайт
    def call_in_python(msg_out):
        eel.call_in_python(msg_out)

    eel.start("index.html", mode='chrome', size=(640, 400))
    #edge, opera, electron, custom, none, false