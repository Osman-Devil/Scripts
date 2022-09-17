import re

txt = 'Погода 23.01.2021 была отличная!_Зато за день до этого (22/01/2021) - очень холодно. '
# pattern = re.compile(r'го')

# pattern = re.compile(r'\d') # одна любая цифра ['2', '3', '0', '1'] селектор
# pattern = re.compile(r'\d+') # 1 или более цифр ['23', '01', '2021', '22', '01', '2021'] квантификатор
# pattern = re.compile(r'\d?') # 0 или 1 ['', '', '', '', '', '', '', '2', '3', '', '0', '1']
# pattern = re.compile(r'\d*')  # 0 или несколько ['', '', '', '', '', '', '', '23', '', '01', '', '2021']
# pattern = re.compile(r'\d{2,4}') # от скольких до скольких цифр включить в группу
# pattern = re.compile(r'\d{2,}')


# pattern = re.compile(r'\w+') # буквы, цифры, нижнее подчеркивание. Плюс ищет слова через пробелы
# pattern = re.compile(r'\s+') # пробельные символы
# pattern = re.compile(r'.') # любой символ
# pattern = re.compile(r'\.') # точка
# pattern = re.compile(r'[а-пя,]') # символы от а до п и символ я
# pattern = re.compile(r'[^а-пя,]') # кроме символов от а до п и символа я
pattern = re.compile(r'^[а-п,о]') # С начала текста символы от а до п и символ я


all_result = pattern.findall(txt)
print(all_result)
# result = pattern.finditer(txt)
# print(*result)
