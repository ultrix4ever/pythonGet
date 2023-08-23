
# Считываем размер квадратной матрицы
n = int(input())
sum = 0

# Создаём пустую матрицу

matrix = [["" for j in range(n)] for i in range(n)]

# Заполняем матрицу элементами из ввода

# Построчно через пробел
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)



# for i in range(n):
#     for j in range(n):
#         matrix[i][j] = input()

# Считаем сумму главной диагонали 

for i in range(n):
    sum += int(matrix[i][i])

print(sum)