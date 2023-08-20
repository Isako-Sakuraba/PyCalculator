
class Calculator:
    history = []  # История всех действий
    history_current = ['', '']  # История действий для текущего примера
    history_max = 6  # Максимальное число действий в истории (сколько действий калькулятор запоминает в память)
    number_left = 0  # Число из которого вычитаем / которое делим, умножаем, складываем
    number_right = 0  # Число на которое делим, умножаем / которое вычитаем, прибавляем
    number_cache = ''  # Временная переменная для записи числа по кнопкам
    action_main = ''  # Действие с помощью знака между number_left и number_right
    result = 0

    # Добавляет цифру к текущему числу
    def add_digit_to_number(self, digit):
        self.number_cache += digit

    # Применяет ввод пользователя к левому числу
    def apply_number_cache_left(self):
        self.number_left = int(self.number_cache)
        self.number_cache = ''

    # Применяет ввод пользователя к правому числу
    def apply_number_cache_right(self):
        self.number_right = int(self.number_cache)
        self.number_cache = ''

    # Записывает действие, которое мы хотим сделать с числами. Нужно привязать к кнопке с действием
    def add_action(self, action):
        self.action_main = action

    # Полностью очищает калькулятор кроме памяти
    def clear(self):
        self.history_current = ['', '']  # История действий для текущего примера
        self.number_left = 0  # Число из которого вычитаем / которое делим, умножаем, складываем
        self.number_right = 0  # Число на которое делим, умножаем / которое вычитаем, прибавляем
        self.number_cache = ''  # Временная переменная для записи числа по кнопкам
        self.action_main = ''  # Действие с помощью знака между number_left и number_right
        self.result = 0

    # Рассчитывает и возвращает результат
    # TODO: Можно ли оптимизировать?
    def calculate(self):

        if self.action_main == '+':
            self.result = self.number_left + self.number_right
        elif self.action_main == '-':
            self.result = self.number_left - self.number_right
        elif self.action_main == '*':
            self.result = self.number_left * self.number_right
        elif self.action_main == '/':
            self.result = self.number_left / self.number_right
        else:
            self.result = -1

        # Обновление истории
        self.history.insert(0, [self.number_left, self.action_main, self.number_right, self.result])
        self.history = self.history[:self.history_max]

        self.clear(self)
