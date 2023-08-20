from tkinter import *
from tkinter import ttk
from calculator import *

# Создание окна
window = Tk()
window.geometry("360x480")
window.title("Калькулятор")

# Сам калькулятор
Calc = Calculator

# Создание текстового поля для истории и расчетов
HistoryLabel = ttk.Label(window, text=Calc.number_cache, anchor='e', font=("Arial", 18), foreground="#A9A9A9")
CalculatorLabel = ttk.Label(window, text="0", anchor='e', font=("Arial", 28))
HistoryLabel.grid(row=0, column=0, columnspan=4)
CalculatorLabel.grid(row=1, column=0, columnspan=4)


# Функции для обработки кнопок и интерфейса
def add_digit(digit, label, history_label):
    if digit.isdigit() and not (digit == '0' and Calc.number_cache == ''):
        Calc.add_digit_to_number(Calc, digit)
        label['text'] = Calc.number_cache
        history_label['text'] = f'{Calc.history_current[0]} {Calc.history_current[1]}'


def commit_action(act, label, label_clear):
    if not Calc.number_cache.isdigit():
        Calc.number_cache = '0'
    if Calc.action_main == '':
        Calc.apply_number_cache_left(Calc)
        Calc.add_action(Calc, act)
        Calc.history_current[0] = Calc.number_left
        Calc.history_current[1]= Calc.action_main
        label['text'] = f'{Calc.history_current[0]} {Calc.history_current[1]}'
        label_clear['text'] = '0'


def calculate(label, history_label):
    if not Calc.number_cache.isdigit():
        Calc.number_cache='0'
    if Calc.action_main != '':
        Calc.apply_number_cache_right(Calc)
        Calc.calculate(Calc)
        history_label['text'] = f'{Calc.history[0][0]} {Calc.history[0][1]} {Calc.history[0][2]} ='
        label['text'] = Calc.history[0][3]


def clear_everything(label, history_label):
    Calc.clear(Calc)
    history_label['text'] = ''
    label['text'] = '0'


# ---Кнопки калькулятора---

ttk.Button(text="7", command=lambda: add_digit('7', CalculatorLabel, HistoryLabel)).grid(column=0, row=2, stick='wens')
ttk.Button(text="8", command=lambda: add_digit('8', CalculatorLabel, HistoryLabel)).grid(column=1, row=2, stick='wens')
ttk.Button(text="9", command=lambda: add_digit('9', CalculatorLabel, HistoryLabel)).grid(column=2, row=2, stick='wens')
ttk.Button(text="+", command=lambda: commit_action('+', HistoryLabel, CalculatorLabel)).grid(column=3, row=2,
                                                                                             stick='wens')
ttk.Button(text="4", command=lambda: add_digit('4', CalculatorLabel, HistoryLabel)).grid(column=0, row=3, stick='wens')
ttk.Button(text="5", command=lambda: add_digit('5', CalculatorLabel, HistoryLabel)).grid(column=1, row=3, stick='wens')
ttk.Button(text="6", command=lambda: add_digit('6', CalculatorLabel, HistoryLabel)).grid(column=2, row=3, stick='wens')
ttk.Button(text="-", command=lambda: commit_action('-', HistoryLabel, CalculatorLabel)).grid(column=3, row=3,
                                                                                             stick='wens')
ttk.Button(text="1", command=lambda: add_digit('1', CalculatorLabel, HistoryLabel)).grid(column=0, row=4, stick='wens')
ttk.Button(text="2", command=lambda: add_digit('2', CalculatorLabel, HistoryLabel)).grid(column=1, row=4, stick='wens')
ttk.Button(text="3", command=lambda: add_digit('3', CalculatorLabel, HistoryLabel)).grid(column=2, row=4, stick='wens')
ttk.Button(text="*", command=lambda: commit_action('*', HistoryLabel, CalculatorLabel)).grid(column=3, row=4,
                                                                                             stick='wens')
ttk.Button(text="CE", command=lambda: clear_everything(CalculatorLabel, HistoryLabel)).grid(column=0, row=5,
                                                                                            stick='wens')
ttk.Button(text="0", command=lambda: add_digit('0', CalculatorLabel, HistoryLabel)).grid(column=1, row=5, stick='wens')
ttk.Button(text="=", command=lambda: calculate(CalculatorLabel, HistoryLabel)).grid(column=2, row=5, stick='wens')
ttk.Button(text="/", command=lambda: commit_action('/', HistoryLabel, CalculatorLabel)).grid(column=3, row=5,
                                                                                             stick='wens')

for row in range(6):
    window.grid_rowconfigure(row, weight=1)

for col in range(4):
    window.grid_columnconfigure(col, weight=1)

window.mainloop()
