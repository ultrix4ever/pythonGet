
n, m = int(input()), int(input())

# Создаем пустую матрицу нужного размера
matrix = [["" for j in range(m)] for i in range(n)]

# Заполняем матрицу элементами из ввода
for i in range(n):
    for j in range(m):
        matrix[i][j] = input()

# Выводим матрицу
for c in range(n):
    for r in range(m):
        print(matrix[c][r], end=' ')
    print()

print()

for c in range(m):
    for r in range(n):
        print(matrix[r][c], end=' ')
    print()
