
tim = input()
rus = input()

def perebor():
    if rus == 'камень' and tim == 'ножницы':
        result = 'Руслан'
    elif rus == 'бумага' and tim == 'камень':
        result = 'Руслан'
    elif rus == 'ножницы' and tim == 'бумага':
        result = 'Руслан'
    else:
        result = 'Тимур'
    if rus == tim:
        result = 'ничья'
    return result
    
print(perebor())
