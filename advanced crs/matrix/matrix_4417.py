def main():
    n = int(input())
    
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    upper_sum = sum(matrix[i][j] for i in range(n // 2) for j in range(i + 1, n - i - 1))
    lower_sum = sum(matrix[i][j] for i in range(n // 2 + 1, n) for j in range(n - i, i))
    right_sum = sum(matrix[i][j] for i in range(n) for j in range(n // 2, n) if i < j and i > n - j - 1)
    left_sum = sum(matrix[i][j] for j in range(n // 2 - 1, -1, -1) for i in range(j + 1, n - j - 1))

    print("Верхняя четверть:", upper_sum)
    print("Правая четверть:", right_sum)
    print("Нижняя четверть:", lower_sum)
    print("Левая четверть:", left_sum)

if __name__ == "__main__":
    main()