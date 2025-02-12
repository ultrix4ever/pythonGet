import random

n = 10**6       # количество испытаний

import random

def is_point_in_figure(x, y):
    """
    Проверяет, находится ли точка (x, y) внутри заданной фигуры.
    
    Условия:
    -2 <= x <= 2
    -2 <= y <= 2
    x^3 + y^4 + 2 >= 0
    3x + y^2 <= 2
    """
    return (-2 <= x <= 2 and 
            -2 <= y <= 2 and 
            x**3 + y**4 + 2 >= 0 and 
            3*x + y**2 <= 2)

def monte_carlo_area_estimation(n):
    """
    Вычисляет площадь фигуры с помощью метода Монте-Карло.
    
    :param num_samples: количество случайных точек
    :return: оценка площади фигуры
    """
    inside_count = 0
    rect_area = 16  # Площадь прямоугольника (-2, 2) x (-2, 2)

    for _ in range(n):
        x = random.uniform(-2, 2)
        y = random.uniform(-2, 2)
        
        if is_point_in_figure(x, y):
            inside_count += 1

    # Оценка площади фигуры
    figure_area = (inside_count / n) * rect_area
    return figure_area

if __name__ == "__main__":
    n = 10**6  # Количество случайных точек для оценки
    estimated_area = monte_carlo_area_estimation(n)
    print(estimated_area)