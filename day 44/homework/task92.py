def GCD(num1, num2):
    if num1 > num2:
        count = num2
    else:
        count = num1
    while count > 0:
        if num1 % num2 == 0 or num2 % num1 == 0:
            if num1 % num2 == 0:
                return num2
            elif num2 % num1 == 0:
                return num1
        else:
            if count != num1:
                if num1 % count == 0:
                    return count
                else:
                    count -= 1
            elif count != num2:
                if num2 % count == 0:
                    return count
                else:
                    count -= 1
print(GCD(4, 10))

# ალბათ უფრო ადვილადაც შეიძლებოდა (:>)
                