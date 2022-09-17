class ExceptionError:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите числовое выражение и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                repeat = input(f'Попробовать еще раз?, напишите "Да" чтобы продолжить "Стоп" чтобы выйти ')

                if repeat.lower() == 'да':
                    print(try_except.my_input())
                elif repeat.lower() == 'стоп':
                    return f'Цикл завершен'
                else:
                    return f'Цикл завершен'


try_except = ExceptionError()
print(try_except.my_input())
