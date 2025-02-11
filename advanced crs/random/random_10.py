import random

def generate_bingo_card():
    # Генерируем список из 24 случайных уникальных чисел от 1 до 75
    numbers = random.sample(range(1, 76), 24)
    
    # Создаем карточку размером 5x5 с нулём в центре
    card = [[0] * 5 for _ in range(5)]
    card[2][2] = 0  # Убедимся, что центральная клетка равна 0
    
    index = 0
    for i in range(5):
        for j in range(5):
            if i == 2 and j == 2:  # Пропускаем центральную клетку
                continue
            card[i][j] = numbers[index]
            index += 1
    
    return card

def print_bingo_card(card):
    for row in card:
        line = ' '.join(str(num).ljust(3) if num != 0 else ' 0 '.center(3) for num in row)
        print(line)

def main():
    bingo_card = generate_bingo_card()
    print("Сгенерированная карточка для игры в бинго:")
    print_bingo_card(bingo_card)

if __name__ == "__main__":
    main()