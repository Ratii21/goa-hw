def cube_checker(volume, side):
    if volume <= 0 or side <= 0:
        return False
    return side ** 3 == volume