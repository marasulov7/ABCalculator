#  A/B Calculator
import tkinter as tk

# Функция закрытия окна
def do_close():
    root.destroy()

# Создание главного окна
root=tk.Tk()
root.geometry("280x300")
root.title("A/B Calculator")

# Добавление метки заголовка
lbl_title = tk.Label(text="А/В Калькулятор", font=('Helvetica', 16, 'bold'), fg='#0000cc') #fg-цвет текста
lbl_title.place(x=55, y=20)

# Добавление кнопки "Рассчитать"
btn_process = tk.Button(root, text="Рассчитать", font = ('Helvetica', 10, 'bold'))
btn_process.place(x=25, y=250, width=90, height=30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text = "Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close) # шрифт, размер, жирный+вызов ф закр окна
btnClose.place(x=160, y=250, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()

