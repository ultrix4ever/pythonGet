def generate_pascal_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def get_pascal_row(triangle, row_index):
    return triangle[row_index]

row_index = int(input())
n = row_index + 1
triangle = generate_pascal_triangle(n)

row = get_pascal_row(triangle, row_index)
print(row)