a, b,c  = int(input()), int(input()), int(input())

def is_valid_triangle(a, b, c):
    if a < (b + c) and b < (a + c) and c < (a + b):
        return True
    else:
        return False

<<<<<<< HEAD
print(is_valid_triangle(a, b, c))
=======
print(is_valid_triangle(a, b, c))

>>>>>>> 6336e4ad89b545ab4e90087cf05f613c3ab81bce
