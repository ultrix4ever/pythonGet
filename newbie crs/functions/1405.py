# объявление функции
def get_month(language, number):
    ru_month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    eng_month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if lan == 'ru':
        return ru_month[number-1]
    else:
        return eng_month[number-1]
# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))



