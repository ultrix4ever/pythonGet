def main():
    n, m = map(int, input().split())
    matrix_1 = []
    matrix_2 = []
    result_matrix = []

    for i in range(n):
        row = list(map(int, input().split()))
        matrix_1.append(row)

    input()  # вставляем пустую строку

    for i in range(n):
        row = list(map(int, input().split()))
        matrix_2.append(row)

    # вычисляем сумму матриц
    for i in range(n):
        row_sum = []
        for j in range(m):
            row_sum.append(matrix_1[i][j] + matrix_2[i][j])
        result_matrix.append(row_sum)

    # печатаем результат
    for row in result_matrix:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()