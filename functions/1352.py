# считываем данные
num = int(input())

<<<<<<< HEAD
# объявление функции поиска простых чисел
=======
# объявление функции
>>>>>>> 6336e4ad89b545ab4e90087cf05f613c3ab81bce
def is_prime(num):
    flag = True
    for i in range(2, num//2 + 1):
        if num % i == 0:
            flag = False
    if num > 1 and flag == True:
        return True
    else:
        return False
<<<<<<< HEAD
    
# объявление функции поиска следующего простого числа после введенного
def get_next_prime(num):
    while is_prime(num+1) == False:
        num += 1
    return num
          
        
# вызываем функцию
print(get_next_prime(num)+1)
=======
        
# вызываем функцию
print(is_prime(num))
>>>>>>> 6336e4ad89b545ab4e90087cf05f613c3ab81bce
