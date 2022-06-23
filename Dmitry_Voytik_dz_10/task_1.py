a = [[3, 2, -6, 7], [4, 2, 0, 8], [3, 2, 1, 8]]
b = [[3, 5, 9, 4], [5, 4, 1, 8], [6, 7, 3, 4]]


class Matrix(object):
    def __init__(self, list_lists):
        self.list_lists = list_lists

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in h]) for h in self.list_lists]))

    def __add__(self, other):
        return Matrix([map(sum, zip(*j))
                       for j in zip(self.list_lists, other.list_lists)])


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f"Sum matrices:\n{matrix_1 + matrix_2}")
