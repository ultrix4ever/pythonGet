import math

def find_largest_fraction(n):
    # Инициализируем переменные для хранения наибольшей правильной несократимой дроби
    max_numerator = 0
    max_denominator = 1
    
    # Перебираем все возможные числители (от 1 до n-1)
    for numerator in range(1, n):
        denominator = n - numerator
        
        # Проверяем условие правильной дроби и несократимости
        if numerator < denominator and math.gcd(numerator, denominator) == 1:
            # Обновляем наибольшую дробь, если нашли более подходящую
            if numerator / denominator > max_numerator / max_denominator:
                max_numerator = numerator
                max_denominator = denominator
    
    return f"{max_numerator}/{max_denominator}"

def main():
    try:
        n = int(input("Введите натуральное число n: "))
        if n < 2:
            raise ValueError("Число должно быть больше 1.")
        
        result = find_largest_fraction(n)
        print(f"Наибольшая правильная несократимая дробь с суммой числителя и знаменателя, равной {n}: {result}")
    
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()