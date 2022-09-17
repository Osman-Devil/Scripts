import json
import sys

with open('users.csv', "r", encoding='utf-8') as f1:
    with open('hobby.csv', "r", encoding='utf-8') as f2:
        for line1 in f1:
            line2 = f2.readline()
            a = dict(zip(line1.split(), line2.split()))

            if not line2:
                line2 = None
            if line1 not in a:
                a[line1.strip()] = line2
            print(a)

            with open('file3.json', 'a', encoding='utf-8') as f:
                for line in a:
                    json.dump(a, f, ensure_ascii=False, indent=4)

        content = f2.read()
        if content:
            sys.exit(1)
