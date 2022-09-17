res = []
with open('nginx_logs.txt', "r", encoding='utf-8') as f:
    for line in f:
        content = line.split()
        res.append((content[0], content[5].strip('"'), content[6]))
    print(res)
