
tim = input()
rus = input()

def perebor():
    if rus == tim:
        result = 'ничья'
    if rus == 'камень' and tim == 'ножницы':
        result = 'Руслан'
    if rus == 'бумага' and tim == 'камень':
        result = 'Руслан'
    else:
        result = 'Тимур'
    return result
    
print(perebor())