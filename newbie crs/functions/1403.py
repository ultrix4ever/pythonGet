import math

# объявление функции
def compute_binom(n, k):
    b = math.factorial(n) / (math.factorial(k)*math.factorial(n-k)) 
    b = int(b)
    return b

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))



