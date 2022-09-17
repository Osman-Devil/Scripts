# №5
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes():
    rand_word = []
    for _ in nouns, adverbs, adverbs:
        sampling1 = random.choice(nouns)
        sampling2 = random.choice(adverbs)
        sampling3 = random.choice(adjectives)
        joke = sampling1 + " " + sampling2 + " " + sampling3
    rand_word.append(joke)
    print(rand_word)
    repeat = input("Еще одну шутку, Да/Нет ?:")
    if repeat == "Да":
        return get_jokes()
    elif repeat == "Нет":
        return "Ладно, оставлю в покое"
    else:
        return "Да или Нет?"

print(get_jokes())