from collections import Counter

d = []
with open('nginx_logs.txt', "r", encoding='utf-8') as f:
    for line in f:
        content = line.split()
        el = content[0]
        d.append(el)
    result = dict(Counter(d))
    v = max(result.values())
    print(list(result.keys())[list(result.values()).index(v)], "Этот ip адрес проспамил нас", v, "раз")
