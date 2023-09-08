numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1,)
def multiply(numbers):  
    result = 1
    for num in numbers:
        result *= num
    return result
print(multiply(numbers))



