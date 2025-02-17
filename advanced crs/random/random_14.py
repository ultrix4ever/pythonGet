import random

def estimate_pi(num_samples):
    inside_circle = 0
    
    for _ in range(num_samples):
        # Генерируем случайные координаты x и y в диапазоне от 0 до 1
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        
        # Проверяем, находится ли точка внутри четверти круга радиусом 1
        if x**2 + y**2 <= 1:
            inside_circle += 1
    
    # Вычисляем приближение для π
    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate

if __name__ == "__main__":
    num_samples = 10**6  # Количество случайных точек для оценки
    estimated_pi = estimate_pi(num_samples)
    print(f"Оцененное значение π с {num_samples} выборками: {estimated_pi}")