import random

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]



def shuffle_matrix(matrix):
    # Сначала преобразуем матрицу в одномерный список
    flat_list = [item for sublist in matrix for item in sublist]
    
    # Перемешиваем одномерный список с помощью random.shuffle
    random.shuffle(flat_list)
    
    # Восстанавливаем структуру двумерного списка
    row_length = len(matrix[0])
    shuffle_matrix = [flat_list[i:i + row_length] for i in range(0, len(flat_list), row_length)]
    
    return shuffle_matrix

matrix = shuffle_matrix(matrix)

