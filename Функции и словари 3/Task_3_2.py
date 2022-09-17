# №2
def num_translate_title(language_t):
    numerate_t = {
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
    if language_t.istitle() and numerate_t.get(language_t.lower()):
        return numerate_t.get(language_t.lower()).title()
    else:
        return numerate_t.get(language_t)
    # if result := numerate_t.get(language_t.lower()):
    # return result if language_t.islower() else result.title()


a = input("num_translate_adv:")
print(num_translate_title(a))
