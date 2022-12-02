# объявление функции
def is_magic(date):
    list_date = date.split('.')
    a = int(list_date[0])*int(list_date[1])
    b = int(list_date[2][2:])
    if a == b:
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))


