def process_complex_numbers():
    try:
        # Ввод первого комплексного числа
        complex1 = complex(input("Введите первое комплексное число (например, 3+4j): "))
        
        # Ввод второго комплексного числа
        complex2 = complex(input("Введите второе комплексное число (например, 2-1j): "))

        # Вычисление суммы, разности и произведения
        sum_result = complex1 + complex2
        difference_result = complex1 - complex2
        product_result = complex1 * complex2

        # Вывод результатов
        print(complex1, "+", complex2, "=", sum_result) 
        print(complex1, "-", complex2, "=", difference_result)
        print(complex1, "*", complex2, "=", product_result)

    except ValueError:
        print("Ошибка: неверный формат ввода. Проверьте, что вы ввели комплексное число в формате a+bj или a-bj.")

def main():
    process_complex_numbers()

if __name__ == "__main__":
    main()