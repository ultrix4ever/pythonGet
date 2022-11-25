# считываем данные
num = int(input())

# объявление функции поиска простых чисел
def is_prime(num):
    flag = True
    for i in range(2, num//2 + 1):
        if num % i == 0:
            flag = False
    if num > 1 and flag == True:
        return True
    else:
        return False
    
# объявление функции поиска следующего простого числа после введенного
def get_next_prime(num):
    while is_prime(num+1) == False:
        num += 1
    return num
          
        
# вызываем функцию
print(get_next_prime(num)+1)
