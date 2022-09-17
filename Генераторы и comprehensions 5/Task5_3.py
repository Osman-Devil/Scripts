# №3
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def gen_in_classes():
    i = 0
    j = 0
    while i < len(klasses):
        if i >= len(tutors):
            yield klasses[i],  None
            i += 1
            j += 1
        else:
            yield tutors[j], klasses[i]
            i += 1
            j += 1


for person in gen_in_classes():
    print(person)

print(type(gen_in_classes()))

