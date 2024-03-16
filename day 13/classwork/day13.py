#cntrl + shift + L - ეს გამოიყენება ყველას მოსანიშნად

#1
num1 = int(input("enter any number: "))

if num1 > 0:
    print("number is positive")
elif num1 < 0:
    print("number is negative")
else:
    print("number equals 0")

#2
age = int(input("enter you age: "))

if age >= 0 and age  < 18:
    print("you are a child")
elif age >= 18 and age < 50:
    print("you are an adult")
else:
    print("you are an old")