
import math

# ввод значений x и y с формы
x = int(input("Введите значение x: "))
y = int(input("Введите значение y: "))

# создание матрицы Aij
A = [[0] * y for _ in range(x)]

# заполнение матрицы Aij
for i in range(x):
    for j in range(y):
        if i > 2:
            if j == 0:
                A[i][j] = 0
            else:
                A[i][j] = 5 * math.atan(i * math.pi / j + 0.983)
        else:
            A[i][j] = x + (x ** 3) / math.factorial(j + 1)

# вывод матрицы Aij
for i in range(x):
    for j in range(y):
        print(A[i][j], end=" ")
    print()

# подсчет количества отрицательных элементов в столбцах
negatives = [0] * y
for j in range(y):
    for i in range(x):
        if A[i][j] < 0:
            negatives[j] += 1

# вывод номера столбца и количества отрицательных элементов
for j in range(y):
    print("Столбец", j + 1, "- количество отрицательных элементов:", negatives[j])

# сортировка побочной диагонали по возрастанию
diagonal = [A[i][y - i - 1] for i in range(min(x, y))]
diagonal.sort()

# замена элементов на побочной диагонали отсортированными значениями
for i in range(min(x, y)):
    A[i][y - i - 1] = diagonal[i]

# вывод отсортированной матрицы Aij
for i in range(x):
    for j in range(y):
        print(A[i][j], end=" ")
    print()

# запись в файл
with open("output.txt", "w") as file:
    for i in range(x):
        for j in range(y):
            file.write(str(A[i][j]) + " ")
        file.write("\n")
