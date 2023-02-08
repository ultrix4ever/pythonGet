# объявление функции
def print_digit_sum(num):
    numbers = [int(i) for i in str(num)]
    print(sum(numbers))

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)