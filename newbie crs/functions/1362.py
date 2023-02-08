# объявление функции
def get_circle(radius):
    import math
    C = 2*math.pi*r
    S = math.pi*r**2
    return C, S

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)