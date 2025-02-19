from fractions import Fraction

def process_fractions(original_fraction1, original_fraction2):
    # Преобразуем строки в объекты Fraction для вычислений
    frac1 = Fraction(*map(int, original_fraction1.split('/')))
    frac2 = Fraction(*map(int, original_fraction2.split('/')))
    
    # Вычисляем сумму, разность, произведение и частное
    sum_result = frac1 + frac2
    difference_result = frac1 - frac2
    product_result = frac1 * frac2
    
    # Обработка деления на ноль
    if frac2 == 0:
        quotient_result = "Нельзя делить на ноль"
    else:
        quotient_result = frac1 / frac2
    
    # Выводим результаты, используя оригинальные дроби для вывода
    print(f"{original_fraction1} + {original_fraction2} = {sum_result}")
    print(f"{original_fraction1} - {original_fraction2} = {difference_result}")
    print(f"{original_fraction1} * {original_fraction2} = {product_result}")
    print(f"{original_fraction1} / {original_fraction2} = {quotient_result}")

def main():
    # Ввод двух дробей от пользователя
    fraction1 = input()
    fraction2 = input()

    try:
        process_fractions(fraction1, fraction2)
    except ValueError as e:
        print("Ошибка: неверный формат дроби. Убедитесь, что вы вводите дробь в формате a/b.")

if __name__ == "__main__":
    main()