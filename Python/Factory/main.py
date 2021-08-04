from Factory import Factory
import tkinter as tk

window = tk.Tk()
window.title("Fabrica")
g = tk.Canvas(window, width=480, height=320, bg='DarkGreen')
g.pack()
f = Factory()


def new_game():
    g.delete('all')
    for i in f.Race:
        unit = f.new_unit(i)
        unit.console()
        file = tk.PhotoImage(file=unit.file)
        i.image = file
        g.create_image(unit.pos, image=i.image)
        g.create_text(unit.pos, text=unit.pos, fill='lime')


button = tk.Button(window, text='Обновить', font=16, command=new_game)
button.pack()
window.mainloop()
