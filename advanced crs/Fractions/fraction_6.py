from fractions import Fraction

def factorial(k):
    """Вычисляет факториал числа k."""
    if k == 0 or k == 1:
        return 1
    result = 1
    for i in range(2, k + 1):
        result *= i
    return result

def sum_of_series(n):
    """Вычисляет сумму ряда 1/1! + 1/2! + ... + 1/n!."""
    total_sum = Fraction(0)

    for k in range(1, n + 1):
        # Вычисляем факториал k
        k_factorial = factorial(k)
        # Добавляем дробь к общей сумме
        total_sum += Fraction(1, k_factorial)

    return total_sum

def main():
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