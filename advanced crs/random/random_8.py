import random

def generate_unique_lottery_numbers(count=100, digits=7):
    unique_numbers = set()

    while len(unique_numbers) < count:
        number = random.randint(10**(digits - 1), 10**digits - 1)
        unique_numbers.add(number)

    return sorted(unique_numbers)

def main():
    lottery_numbers = generate_unique_lottery_numbers()
    
    for number in lottery_numbers:
        print(f"{number:07d}")  # Форматируем число с ведущими нулями, если необходимо

if __name__ == "__main__":
    main()