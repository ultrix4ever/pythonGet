import random

def assign_secret_friends(students):
    # Создаем копию списка студентов для случайной перестановки
    shuffled_students = students.copy()
    random.shuffle(shuffled_students)
    
    # Проверяем, что никто не оказался своим тайным другом
    while any(students[i] == shuffled_students[i] for i in range(len(students))):
        random.shuffle(shuffled_students)
    
    # Создаем словарь для хранения соответствий
    secret_friends = {}
    for original, secret in zip(students, shuffled_students):
        secret_friends[original] = secret
    
    return secret_friends

def main():
    n = int(input("Введите количество учеников: "))
    
    students = []
    for _ in range(n):
        name = input().strip()
        students.append(name)
    
    # Назначаем тайных друзей
    secret_friends = assign_secret_friends(students)
    
    # Выводим результаты
    for student in students:
        print(f"{student} - {secret_friends[student]}")

if __name__ == "__main__":
    main()