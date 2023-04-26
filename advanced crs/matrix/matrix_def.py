
n = 8
matrix = [[1]*n for _ in range(n)]


# Используйте функцию print_matrix() для вывода квадратной матрицы размерности n

def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

print_matrix(matrix, n)

# Для считывания матрицы из n строк, заполненной числами, удобно использовать следующий код:

n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

print_matrix(matrix, n)

# Считать матрицу в обратном порядке
n = 3
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

for i in range(n):
    for j in range(n):
        print(a[n - i - 1][n - j - 1], end=' ')
    print()