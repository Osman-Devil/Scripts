# №1
def nums_generator(n=20):
    for code in range(1, n + 1):
        if code % 2 == 1:
            yield code


numbers = nums_generator()
print(*numbers)
print(type(numbers))