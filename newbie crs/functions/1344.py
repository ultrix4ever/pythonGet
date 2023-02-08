# объявление функции создание списка делителей
def get_factors(n):
    l = []
    for i in range(1,n+1):
        if n % i == 0:
            l.append(i)
    return l

# объявылоение функции подсчета колличества делителей
def number_of_factors(n):
    return len(get_factors(n))

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
