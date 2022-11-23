# объявление функции
def solve(a, b, c):
    import math
    D = b**2 - 4 * a * c
    if D >= 0:
        x1 = ((-b + math.sqrt(D)) / (2 * a))
        x2 = ((-b - math.sqrt(D)) / (2 * a))
        if x1 >= x2:
            return x2, x1
        else:
            return x1, x2

    
# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)







