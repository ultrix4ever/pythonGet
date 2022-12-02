<<<<<<< HEAD
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
=======
text = input()
text1 =''
for i in range(0, len(text)):
    if text[i].isupper() == True:
        text1 += '_'
    text1 += text[i].lower()
text = text1[1:]


print(text)
>>>>>>> 6336e4ad89b545ab4e90087cf05f613c3ab81bce
