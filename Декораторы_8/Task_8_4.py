from functools import wraps


def val_checker(callback):
    def val_caller(call):
        @wraps(call)
        def wrapper(*args):
            for el in args:
                if not callback(el):
                    raise ValueError(f'Wrong val {el}')
            return call(*args)
        return wrapper
    return val_caller


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(1)
print(a)
a = calc_cube(-1)
print(a)
