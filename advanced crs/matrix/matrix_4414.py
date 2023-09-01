# Считываем размер квадратной матрицы
n = int(input())
sum = 0
sr = 0
count = 0
sum_str = 0
# Создаём пустую матрицу
# matrix = [["" for j in range(n)] for i in range(n)]

# Заполняем матрицу элементами из ввода
# Построчно через пробел
matrix = []
sum_list = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in row:
        sum_str += j
    sum_list.append(sum_str) 
    sum_str = 0
    matrix.append(row)

# Считаем среднее каждой строки и суммируем числа больше среднего в строке

for i in range(n):
    count = 0
    for j in range(n):
        sum += matrix[i][j]
#        print(matrix[i][j])
#        print(sum_list[j] / n)
        if matrix[i][j] > sum_list[i] / n:
            count += 1
    print(count)
