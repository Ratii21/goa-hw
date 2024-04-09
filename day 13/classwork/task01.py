age = int(input("enter you age: "))

if age >= 0 and age  < 18:
    print("you are a child")
elif age >= 18 and age < 50:
    print("you are an adult")
else:
    print("you are an old")