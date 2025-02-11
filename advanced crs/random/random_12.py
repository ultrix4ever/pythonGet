import random
import string

def generate_password(length):
    # Определяем набор символов для пароля, исключая перепутываемые символы
    allowed_chars = (
        string.ascii_letters + string.digits
    ).replace('l', '').replace('I', '').replace('1', '').replace('o', '').replace('O', '').replace('0', '')
    
    # Генерируем случайный пароль из заданного набора символов
    password = ''.join(random.choice(allowed_chars) for _ in range(length))
    return password

def generate_passwords(count, length):
    # Генерируем список из count случайных паролей
    passwords = [generate_password(length) for _ in range(count)]
    return passwords

def main():
    n = int(input("Введите количество паролей (n): "))
    m = int(input("Введите длину паролей (m): "))

    # Генерируем и выводим список паролей
    passwords = generate_passwords(n, m)
    for password in passwords:
        print(password)

if __name__ == "__main__":
    main()