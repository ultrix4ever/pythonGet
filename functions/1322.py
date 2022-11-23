# объявление функции
def print_fio(name, surname, patronymic):
    name = name[0].upper()
    surname = surname[0].upper()
    patronymic = patronymic[0].upper()
    print(name, surname, patronymic, sep='')

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)

