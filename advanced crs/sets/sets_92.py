
def completed_homework(n, m, k, p):
    # Количество учеников, у которых домашнее задание съела собака ИЛИ отключили свет,
    # это m + k (два отдельных случая), а затем нужно избавиться от п, которые были учтены дважды 
    # (и собака и свет), поэтому отнимаем p
    problems = m + k - p
    # Оставшиеся студенты сделали домашнее задание
    done_homework = n - problems
    return done_homework

# Вызов функции с конкретными значениями
n, m, k, p = int(input()), int(input()), int(input()), int(input())
print(completed_homework(n, m, k, p))
