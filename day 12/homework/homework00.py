budget = int(input("enter your budget: "))
amount_to_spend = int(input("enter amount of money, that you want to spend: "))

if amount_to_spend <= budget:
    print("you can buy it")
else:
    print("you can't buy it")
    