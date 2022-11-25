a, b,c  = int(input()), int(input()), int(input())

def is_valid_triangle(a, b, c):
    if a < (b + c) and b < (a + c) and c < (a + b):
        return True
    else:
        return False

print(is_valid_triangle(a, b, c))