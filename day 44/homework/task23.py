num1 = 10
num2 = 5
for i in range(9999999, -1, -1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
        break

