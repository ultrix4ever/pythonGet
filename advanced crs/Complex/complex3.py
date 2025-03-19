def compute_expression(n, z1, z2):
    # Вычисляем степени комплексных чисел и их сопряжений
    z1_n = z1 ** n
    z2_n = z2 ** n
    z1_conj_n = z1.conjugate() ** n
    z2_conj_n = z2.conjugate() ** (n + 1)
    
    # Вычисляем значение выражения
    result = z1_n + z2_n + z1_conj_n + z2_conj_n

    return result

def main():
    try:
        # Ввод данных
        n = int(input())
        if n <= 0:
            raise ValueError("Число должно быть положительным.")
        
        z1 = complex(input())
        z2 = complex(input())

        # Вычисление и вывод результата
        result = compute_expression(n, z1, z2)
        print(result)

    except ValueError as e:
        print(f"Ошибка: {e}. Проверьте правильность ввода данных.")

if __name__ == "__main__":
    main()
