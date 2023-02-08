# функция проверки на полиндром
def is_palindrome(password):
    password = psw.split(':')
    if password[0] == password[0][::-1]:
        return True
    else:
        return False
# функция проверки на простое число
def is_prime(password):
    password = psw.split(':')
    counter = 0
    num = int(password[1])
    for i in range(2, num//2 + 1):
        if num % i == 0:
            counter +=1
    if counter <=0:
        return True
    else:
        return False

# функция проверки на четность
def is_even(password):
    password = psw.split(':')
    num = int(password[2])
    if num % 2 == 0:
        return True
    else:
        return False

# функция проверки пароля на соответствие

def is_valid_password(password):
    password = psw.split(':')
    if is_even(password) == True and is_prime(password) == True and is_palindrome(password) == True and len(password) == 3:
        return True
    else:
        return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))

