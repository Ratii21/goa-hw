age = int(input("enter you age: "))

if age >= 18:
    print("You can participate in the elections")

else:
    age_before_18 = 18 - age
    print("you need " ,age_before_18, "years to participate in the elections")