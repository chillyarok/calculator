'''imports'''
from tkinter import *
from math import *
from data import data
import webbrowser as web


'''funcs'''
#Функция описывающая меню для заметок
def notes():
    def save():
        g = open("data/notes.txt", "w", )  # encoding="utf=8"
        g.write(t.get(1.0, END))
        g.close()

    henu = Menu()
    tl = Toplevel(menu=henu)
    t = Text(tl)
    t.grid()
    henu.add_command(label="save", command=save)
    g = open("data/notes.txt", "r")
    t.insert("1.0", g.read())
    g.close()

#Функция для отработки нажатия кнопок
def button_click(text):
    global calc_operator
    data.display_data += str(text)
    stringV_displey_data.set(data.display_data)

#Функция удаляющая один последний символ с экрана калькулятора
def button_delete():
    try:
        rf = []
        df = str(stringV_displey_data.get())
        for i in df:
            rf.append(i)
        rf.pop(-1)
        data.display_data = "".join(rf)
        stringV_displey_data.set("".join(rf))
    except:
        pass

#Функция очищающие экран калькулятора
def button_clear():
    data.display_data = ''
    stringV_displey_data.set('')

#Функция кнопки равно
def button_equal():
    data.ans = eval(stringV_displey_data.get())
    button_clear()
    stringV_displey_data.set(data.ans)

#Функция для разсчёта площади триугольника
def triangle():
    def g():
        try:
            f = int(en1.get()) * int(en2.get()) / 2
            Label(Tl, text=f'площадь равна:{f}').grid(row=6, column=0)
            bb = Button(Tl, text="записать в калькулятор", command=lambda: button_click(f))
            bb.grid(row=7, column=0)
        except:
            pass

    Tl = Toplevel()
    Label(Tl, text='введите высоту триугольника').grid(row=0, column=0)
    en1 = Entry(Tl, )
    en1.grid(row=2, column=0)
    Label(Tl, text='введите основание триугольника').grid(row=3, column=0)
    en2 = Entry(Tl, )
    en2.grid(row=4, column=0)
    b = Button(Tl, text="найти", command=g)
    b.grid(row=5, column=0)

#Функция для разсчёта площади трапеции
def trapecia():
    def g():
        try:
            f = ((int(en3.get()) + int(en2.get())) / 2) * int(en1.get())
            Label(Tl, text=f'площадь равна:{f}').grid(row=8, column=0)
            bb = Button(Tl, text="записать в калькулятор", command=lambda: button_click(f))
            bb.grid(row=9, column=0)
        except:
            pass

    Tl = Toplevel()
    Label(Tl, text='введите высоту трапеции').grid(row=0, column=0)
    en1 = Entry(Tl, )
    en1.grid(row=2, column=0)
    Label(Tl, text='введите 1 основание трапеции').grid(row=3, column=0)
    en2 = Entry(Tl, )
    en2.grid(row=4, column=0)
    Label(Tl, text='введите 2 основание трапеции').grid(row=5, column=0)
    en3 = Entry(Tl, )
    en3.grid(row=6, column=0)
    b = Button(Tl, text="найти", command=g)
    b.grid(row=7, column=0)

#Функция для разсчёта площади ромба
def romb():
    def g():
        try:
            f = int(en1.get()) * int(en2.get()) / 2
            Label(Tl, text=f'площадь равна:{f}').grid(row=6, column=0)
            bb = Button(Tl, text="записать в калькулятор", command=lambda: button_click(f))
            bb.grid(row=7, column=0)
        except:
            pass

    Tl = Toplevel()
    Label(Tl, text='введите 1 диагональ ромба').grid(row=0, column=0)
    en1 = Entry(Tl, )
    en1.grid(row=2, column=0)
    Label(Tl, text='введите 2 диагональ ромба').grid(row=3, column=0)
    en2 = Entry(Tl, )
    en2.grid(row=4, column=0)
    b = Button(Tl, text="найти", command=g)
    b.grid(row=5, column=0)

#Функция для разсчёта площади круга
def circle():
    def g():
        try:
            f = (int(en1.get()) ** 2) * pi
            Label(Tl, text=f'площадь равна:{f}').grid(row=4, column=0)
            bb = Button(Tl, text="записать в калькулятор", command=lambda: button_click(f))
            bb.grid(row=5, column=0)
        except:
            pass

    Tl = Toplevel()
    Label(Tl, text='введите радус').grid(row=0, column=0)
    en1 = Entry(Tl, )
    en1.grid(row=2, column=0)
    b = Button(Tl, text="найти", command=g)
    b.grid(row=3, column=0)

#Функция для разсчёта площади прямоугольника
def rectangle():
    def g():
        try:
            f = int(en1.get()) * int(en2.get())
            Label(Tl, text=f'площадь равна:{f}').grid(row=6, column=0)
            bb = Button(Tl, text="записать в калькулятор", command=lambda: button_click(f))
            bb.grid(row=7, column=0)
        except:
            pass

    Tl = Toplevel()
    Label(Tl, text='введите сторону проямогольника').grid(row=0, column=0)
    en1 = Entry(Tl, )
    en1.grid(row=2, column=0)
    Label(Tl, text='введите другую сторону').grid(row=3, column=0)
    en2 = Entry(Tl, )
    en2.grid(row=4, column=0)
    b = Button(Tl, text="найти", command=g)
    b.grid(row=5, column=0)

#Функция с ссылкой на сайт хелпа
def help():
    web.open(url="http://jgjgjgjjgjhjgh.tilda.ws/page33212744.html", new=1)

#В функции описывается меню в верхней части окна
def menu():
    menu = Menu(window)
    squaremenu = Menu(tearoff=0)
    window.config(bg=data.bgcolor, menu=menu)
    menu.add_command(label="заметки", command=notes)
    menu.add_command(label="помощь", command=help)
    menu.add_cascade(label="разсчёт площади", menu=squaremenu)
    squaremenu.add_command(label="прямоугольник", command=rectangle)
    squaremenu.add_command(label="триугольник", command=triangle)
    squaremenu.add_command(label="ромб", command=romb)
    squaremenu.add_command(label="трапеция", command=trapecia)
    squaremenu.add_command(label="круг", command=circle)

#В функции описывается итерфейс
def gui():
    displey = Entry(width=60, font=1000, bd=0, bg=data.color, textvariable=stringV_displey_data, justify=RIGHT)
    displey.grid(row=0, column=0, columnspan=5, pady=data.button_pady)
    b11 = Button(text=7, width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
                 command=lambda: button_click('7'))
    b11.grid(row=1, column=0, pady=data.button_pady)
    b12 = Button(text=8, width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
                 command=lambda: button_click('8'))
    b12.grid(row=1, column=1, pady=data.button_pady)
    b13 = Button(text=9, width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
                 command=lambda: button_click('9'))
    b13.grid(row=1, column=2, pady=data.button_pady)
    b14 = Button(text="AC", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
                 command=button_clear)
    b14.grid(row=1, column=3, pady=data.button_pady)
    b15 = Button(text="del", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
                 command=button_delete)
    b15.grid(row=1, column=4, pady=data.button_pady)

    Button(text=4, width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('4')).grid(row=2, column=0, pady=data.button_pady)
    Button(text=5, width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('5')).grid(row=2, column=1, pady=data.button_pady)
    Button(text=6, width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('6')).grid(row=2, column=2, pady=data.button_pady)
    Button(text="+", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('+')).grid(row=2, column=3, pady=data.button_pady)
    Button(text="-", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('-')).grid(row=2, column=4, pady=data.button_pady)

    Button(text=1, width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('1')).grid(row=3, column=0, pady=data.button_pady)
    Button(text=2, width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('2')).grid(row=3, column=1, pady=data.button_pady)
    Button(text=3, width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('3')).grid(row=3, column=2, pady=data.button_pady)
    Button(text="×", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('*')).grid(row=3, column=3, pady=data.button_pady)
    Button(text="÷", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('/')).grid(row=3, column=4, pady=data.button_pady)

    Button(text="xⁿ", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('**')).grid(row=4, column=0, pady=data.button_pady)
    Button(text="x²", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('**2')).grid(row=4, column=1, pady=data.button_pady)
    Button(text="x³", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('**3')).grid(row=4, column=2, pady=data.button_pady)
    Button(text="ans", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click(data.ans)).grid(row=4, column=3, pady=data.button_pady)
    Button(text="√", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('sqrt(')).grid(row=4, column=4, pady=data.button_pady)

    Button(text="sin", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('sin(')).grid(row=5, column=0, pady=data.button_pady)
    Button(text="cos", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('cos(')).grid(row=5, column=1, pady=data.button_pady)
    Button(text="tg", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('tan(')).grid(row=5, column=2, pady=data.button_pady)
    Button(text="ctg", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('ctan(')).grid(row=5, column=3, pady=data.button_pady)
    Button(text="=", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=button_equal).grid(row=5, column=4, pady=data.button_pady)

    Button(text="0", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('0')).grid(row=6, column=0, pady=data.button_pady)

    Button(text="(", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click('(')).grid(row=6, column=1, pady=data.button_pady)
    Button(text=")", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           command=lambda: button_click(')')).grid(row=6, column=2, pady=data.button_pady)
    Button(text="", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color,
           ).grid(row=6, column=3, pady=data.button_pady)
    Button(text="", width=data.button_width, height=data.button_height, font=data.font, bd=0, bg=data.color
           ).grid(row=6, column=4, pady=data.button_pady)

#функция добавляет разсчёт котангенса(так как данной функции нет в библиотеке math)
def ctan(__x):
    f = 1 / tan(__x)
    return f

#функция создаёт нужные текстовые файлы при их отсутствии(устранение ошибок связанных с тем что нет какого-то файла)
def start():
    g = open("data/notes.txt", "a")
    g.close()


'''gui'''
window = Tk()
window.title("calc")
window.iconbitmap("data/icons8-calculator-96.ico")
window.resizable(0,0)
stringV_displey_data = StringVar()
start()
menu()
gui()
window.mainloop()
