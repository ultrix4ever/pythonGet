import math

def simplify_fraction(m, n):
    # Находим наибольший общий делитель чисел m и n
    gcd_value = math.gcd(m, n)
    
    # Сокращаем числитель и знаменатель на их НОД
    simplified_numerator = m // gcd_value
    simplified_denominator = n // gcd_value
    
    return simplified_numerator, simplified_denominator

def main():
    # Вводим два натуральных числа
    m = int(input("Введите числитель (m): "))
    n = int(input("Введите знаменатель (n): "))
    
    # Проверяем, что числа натуральные
    if m <= 0 or n <= 0:
        print("Оба числа должны быть натуральными.")
        return
    
    # Сокращаем дробь и выводим результат
    simplified_m, simplified_n = simplify_fraction(m, n)
    
    if simplified_n == 1:
        print(f"Сокращенная дробь: {simplified_m}")
    else:
        print(f"Сокращенная дробь: {simplified_m}/{simplified_n}")

if __name__ == "__main__":
    main()