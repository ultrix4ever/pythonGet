# объявление функции
def get_factors(n):
    l = []
    for i in range(1,n+1):
        if n % i == 0:
            l.append(i)
    return l

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))