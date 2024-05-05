x = int(input("enter number that is a multiple of both 2 and 3: "))

while x % 2 != 0 or x % 3 != 0 :
    x = int(input("enter number that is a multiple of both 2 and 3: "))
else:
    print(x)