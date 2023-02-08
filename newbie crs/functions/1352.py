# считываем данные
num = int(input())

# объявление функции
def is_prime(num):
    flag = True
    for i in range(2, num//2 + 1):
        if num % i == 0:
            flag = False
    if num > 1 and flag == True:
        return True
    else:
        return False
        
# вызываем функцию
print(is_prime(num))