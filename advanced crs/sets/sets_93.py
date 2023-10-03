data = input()
len_list = len(list(map(int, data.split())))
print(len_list)
len_set = len(set(list(map(int, data.split()))))
print(len_set)
    # определяем максимальное количество дубликатов
max_duplicates = len_list - len_set

# Тестовые данные

print(max_duplicates)