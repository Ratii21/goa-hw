def sum_of_digits(num):
    num = str(num)
    i = 0
    result = 0
    while i < len(num):
        result += int(num[i])
        i += 1
    print(result)

sum_of_digits(34)