# №3
def thesaurus_adv(*args):
    dictionary = {}
    for word in args:
        dictionary_w = filter(lambda el: el.startswith(word[0]), args)
        dictionary[word[0]] = list(dictionary_w)
        sorted_w = sorted(dictionary.items())
        dictionary = dict(sorted_w)

    return dictionary


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
