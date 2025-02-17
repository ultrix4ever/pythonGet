from decimal import *
num = Decimal(input())

from decimal import Decimal

def sum_max_min_digits(num):
    # Преобразуем Decimal число в строку и удаляем все нецифровые символы (например, точку)
    num_str = str(num).replace('.', '')
    
    # Исключаем возможные отрицательные знаки
    if '-' in num_str:
        num_str = num_str.replace('-', '')

    # Проверяем, что в строке остались цифры
    if not num_str.isdigit():
        raise ValueError("Число содержит недопустимые символы.")
    
    # Находим минимальную и максимальную цифры
    digits = [int(digit) for digit in num_str]
    max_digit = max(digits)
    min_digit = min(digits)
    
    # Возвращаем сумму наибольшей и наименьшей цифр
    return max_digit + min_digit

# Пример использования
try:

    result = sum_max_min_digits(num)
    print(result)
except ValueError as e:
    print(e)

