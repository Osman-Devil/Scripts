class Cell:
    def __init__(self, number_of_cell):
        self.number_of_cell = number_of_cell

    def make_order(self,row_len):
        result = ['*' * row_len] * (self.number_of_cell // row_len)
        if self.number_of_cell % row_len:
            result.append('*' * (self.number_of_cell % row_len))
        return '\n'.join(result)

    def __str__(self):
        return str(self.number_of_cell)

    def __add__(self, other):
        print("Сложение количество ячеек: ")
        return Cell(self.number_of_cell + other.number_of_cell)

    def __sub__(self, other):
        print("Вычитание количество ячеек:")
        if self.number_of_cell < other.number_of_cell:
            raise ValueError("Ячеек в первой клетке меньше второй")
        return Cell(self.number_of_cell - other.number_of_cell)

    def __mul__(self, other):
        print("Произведение количества ячеек:")
        return Cell(self.number_of_cell * other.number_of_cell)

    def __floordiv__(self, other):
        print("Цело-численное деление количества ячеек:")
        return Cell(self.number_of_cell // other.number_of_cell)

    def __truediv__(self, other):
        print("Деление количества ячеек:")
        return Cell(self.number_of_cell / other.number_of_cell)


a = Cell(30)
b = Cell(11)
print(a.make_order(7))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
