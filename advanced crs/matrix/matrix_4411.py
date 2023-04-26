
n, m = int(input()), int(input())

# Создаем пустую матрицу нужного размера
matrix = [["" for j in range(m)] for i in range(n)]

# Заполняем матрицу элементами из ввода
for i in range(n):
    for j in range(m):
        matrix[i][j] = input()

# Выводим матрицу
for row in matrix:
    print(" ".join(row))