from fractions import Fraction

def sum_of_series(n):
    # Инициализируем сумму нулём в виде рационального числа
    total_sum = Fraction(0)

    # Вычисляем сумму ряда 1/1^2 + 1/2^2 + ... + 1/n^2
    for k in range(1, n + 1):
        total_sum += Fraction(1, k**2)
    
    return total_sum

def main():
    # Вводим натуральное число n
    try:
        n = int(input("Введите натуральное число n: "))
        if n <= 0:
            raise ValueError("Число должно быть положительным.")
        
        result = sum_of_series(n)
        print(f"Сумма ряда равна: {result}")
    
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()