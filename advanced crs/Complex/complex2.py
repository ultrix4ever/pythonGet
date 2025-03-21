numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]

# Находим комплексное число с наибольшим модулем
max_complex_number = max(numbers, key=abs)

# Вычисляем модуль этого числа
max_modulus = abs(max_complex_number)

# Выводим результаты на отдельных строках
print(f"Комплексное число с наибольшим модулем: {max_complex_number}")
print(f"Модуль этого числа: {max_modulus}")