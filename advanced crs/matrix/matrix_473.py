def main():
    n = int(input())
    
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    m = int(input())

    result_matrix = pow_matrix(matrix, m)

    for row in result_matrix:
        print(" ".join(map(str, row)))

def multiply_matrices(matrix_1, matrix_2):
    n = len(matrix_1)
    k = len(matrix_2[0])
    
    result_matrix = [[0] * k for _ in range(n)]
    
    for i in range(n):
        for j in range(k):
            for l in range(k):
                result_matrix[i][j] += matrix_1[i][l] * matrix_2[l][j]
                
    return result_matrix

def pow_matrix(matrix, m):
    if m == 1:
        return matrix
    
    if m % 2 == 0:
        temp_matrix = pow_matrix(matrix, m // 2)
        return multiply_matrices(temp_matrix, temp_matrix)
    else:
        return multiply_matrices(matrix, pow_matrix(matrix, m - 1))


if __name__ == "__main__":
    main()