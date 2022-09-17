# №1
def num_translate(language):
    numerate = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'fife': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять'
    }
    return numerate.get(language)


a = input("num_translate_adv:")
print(num_translate(a))








