from copy import deepcopy


class Matrix:
    def __init__(self, a):
        self.a = deepcopy(a)
        self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in a])
        list_1 = []
        for i in a:
            list_1.append([j for j in i])
        self.a = list_1

    def __str__(self):
        self.c = '\n'.join(map(lambda r: '  '.join(map(str,r)), self.a))
        return self.c

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                sum_matrix = other.a[i][j] + self.a[i][j]
                numbers.append(sum_matrix)
                if len(numbers) == len(self.a):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)
