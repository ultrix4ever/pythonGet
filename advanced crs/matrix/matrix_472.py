def main():
    n, m = map(int, input().split())
    
    matrix_1 = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix_1.append(row)
        
    input()  # считываем пустую строку
    
    m, k = map(int, input().split())
    
    matrix_2 = []
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix_2.append(row)

    result_matrix = multiply_matrices(matrix_1, matrix_2)

    for row in result_matrix:
        print(" ".join(map(str, row)))


def multiply_matrices(matrix_1, matrix_2):
    n = len(matrix_1)
    m = len(matrix_1[0])
    k = len(matrix_2[0])
    
    result_matrix = [[0] * k for _ in range(n)]
    
    for i in range(n):
        for j in range(k):
            for l in range(m):
                result_matrix[i][j] += matrix_1[i][l] * matrix_2[l][j]
                
    return result_matrix


if __name__ == "__main__":
    main()