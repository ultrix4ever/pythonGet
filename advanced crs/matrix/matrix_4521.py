def main():
    n = int(input())
    m = int(input())
    
    mult = [[i * j for j in range(m)] for i in range(n)]

    for row in mult:
        for num in row:
            print(str(num).ljust(3), end="")
        print()

if __name__ == "__main__":
    main()