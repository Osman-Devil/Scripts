def type_logger(func):
    def wrapper(*args):
        calculate = func(*args)
        if len(args) >= 1:
            for element in args:
                print(f'{element}: {type(element)}')
        return calculate
    return wrapper


@type_logger
def calc_cube(x, *args):
    return x ** 3


our_list = calc_cube(3)
print(our_list)
our_list = calc_cube(4)
print(our_list)
