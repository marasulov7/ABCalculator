#  A/B Calculator
import tkinter as tk
from tkinter import messagebox as mb
import os
import math

# Функция закрытия окна
def do_close():
    root.destroy()

# Функция форматирования процентов
def num_percent(num):
    return "{:.2f}".format(num*100).rjust(10) + '%'

def do_processing():
    #Считывание данных из полей ввода
    n1 = int(ent_visitors1.get())
    c1 = int(ent_conversions1.get())
    n2 = int(ent_visitors2.get())
    c2 = int(ent_conversions2.get())
    
    #Проверка данных из полей ввода
    if n1<=0 or n2<=0:
        mb.showerror(title='Ошибка', message='Неверное количество посетителей')
        return #если будет ошибка, дальше программа не выполняется
    
    popup_window(n1, c1, n2, c2)

# Функция дополнительного окна
def popup_window(n1, c1, n2, c2):
    window=tk.Toplevel()
    window.geometry("500x500")
    window.title("А/В результат")
    
    # Добавление окна вывода текста
    txtOutput = tk.Text(window, font = ('Courier New', 10, 'bold'))
    txtOutput.place(x=15, y=115, width=470, height=300)
    
    # Добавление заголовка
    txtOutput.insert(tk.END, '                           Контрольная    Тестовая' + os.linesep)
    txtOutput.insert(tk.END, '                           группа         группа' + os.linesep)
    txtOutput.insert(tk.END, '-------------------------------------------------------' + os.linesep)
    
    # Добавление вывода конверсии и стандартного отклонения
    p1=c1/n1
    p2=c2/n2
    txtOutput.insert(tk.END, 'Конверсия              ' + num_percent(p1)
        + '    ' + num_percent(p2) + os.linesep)
    sigma1 = math.sqrt(p1*(1-p1)/n1)
    sigma2 = math.sqrt(p2*(1-p2)/n2)
    txtOutput.insert(tk.END, 'Стандартное отклонение ' + num_percent(sigma1)
        + '    ' + num_percent(sigma2) + os.linesep)
    txtOutput.insert(tk.END, '-------------------------------------------------------' + os.linesep)
    
    # Добавление кнопки закрытия окна
    btnClosePopup = tk.Button(window, text = "Закрыть", font = ('Helvetica', 10, 'bold'), command=window.destroy) 
    btnClosePopup.place(x=190, y=450, width=90, height=30)
    
    # Перевод фокуса на созданное окно
    window.focus_force()

# Создание главного окна
root=tk.Tk()
root.geometry("280x300")
root.title("A/B Calculator")

# Добавление метки заголовка
lbl_title = tk.Label(text="А/В Калькулятор", font=('Helvetica', 16, 'bold'), fg='#0000cc') #fg-цвет текста
lbl_title.place(x=55, y=20)

# Добавление метки заголовка контрольной группы
lbl_title1 = tk.Label(text="Контрольная группа", font=('Helvetica', 12, 'bold'), fg='#0066ff') #fg-цвет текста
lbl_title1.place(x=25, y=55)

# Добавление полей ввода контрольной группы
lbl_visitors1 = tk.Label(text="Посетители", font=('Helvetica', 10, 'bold')) 
lbl_visitors1.place(x=25, y=85)

ent_visitors1 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='center') #justify='center' выравнивание по центру
ent_visitors1.place(x=115, y=85, width=90, height=20)
ent_visitors1.insert(tk.END, "255") #вставка 0 в поле ввода

lbl_conversions1 = tk.Label(text="Конверсии", font=('Helvetica', 10, 'bold')) 
lbl_conversions1.place(x=25, y=115)

ent_conversions1 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='center') 
ent_conversions1.place(x=115, y=115, width=90, height=20)
ent_conversions1.insert(tk.END, "26")

# Добавление метки заголовка тестовой группы
lbl_title2 = tk.Label(text="Тестовая группа", font=('Helvetica', 12, 'bold'), fg='#008800') #fg-цвет текста
lbl_title2.place(x=25, y=145)

# Добавление полей ввода тестовой группы
lbl_visitors2 = tk.Label(text="Посетители", font=('Helvetica', 10, 'bold')) 
lbl_visitors2.place(x=25, y=175)

ent_visitors2 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='center') 
ent_visitors2.place(x=115, y=175, width=90, height=20)
ent_visitors2.insert(tk.END, "235")

lbl_conversions2 = tk.Label(text="Конверсии", font=('Helvetica', 10, 'bold')) 
lbl_conversions2.place(x=25, y=205)

ent_conversions2 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='center') 
ent_conversions2.place(x=115, y=205, width=90, height=20)
ent_conversions2.insert(tk.END, "18")

# Добавление кнопки "Рассчитать"
btn_process = tk.Button(root, text="Рассчитать", font = ('Helvetica', 10, 'bold'), command=do_processing)
btn_process.place(x=25, y=250, width=90, height=30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text = "Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close) # шрифт, размер, жирный+вызов ф закр окна
btnClose.place(x=160, y=250, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()

