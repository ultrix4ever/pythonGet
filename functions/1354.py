# объявление функции
def is_password_good(password):
    if len(txt) >= 8 and password.isalpha() == False and password.isdigit() == False and password!=password.lower() and password!=password.upper():
        return True
    else: 
        return False
    

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))