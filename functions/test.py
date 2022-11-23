def is_prime(password):
    counter = 0
    num = int(password[1])
    for i in range(2, num//2 + 1):
        if num % i == 0:
            counter +=1
    if counter <=0:
        return True
    else:
        return False

txt = input()
password = txt.split(':')
print(is_prime(txt))