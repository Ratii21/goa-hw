#len ფუნქცია გვითვლის თუ რამდენი ელემენტია კოლქციაში
name = ["rati","gio","luka"]
print(len(name))



user_name = input("enter your firsname and lastname: ")
for i in range(0, len(user_name)):
    print(user_name[i])


fullname = input("enter your fullname: ")
for i in range(0, len(fullname), 2):
    print(fullname[i])


#in-ით ჩვენ შეგვიძლია გავიგოთ არის თუ არა კონკრეტული ელემენტი ცოლექციაში
cart = ["banana","apple","melon"]
print("melon" in cart)
#თუ არის გამოიტანს True-ს, ხოლო თუ არ არის გამოიტანს False-ს

#ერთ ტოლობა თითქმის ყველა პროგრამაში გამოიყენება მხოლოდ იმისთვის რომ ცვლადს მივანიჭოთ მნიშვნელობა

numbers = [1,2,3,4,5,6,7,8,9,10]

if 5 in numbers:
    print("Yes 5 is in numbers list")
else:
    print("No 5 is not in numbers list")



numbers = [1,2,3,4,5,6,7,8,9,10]

result = 0

for num in numbers:
    if num % 2 == 0:
        result = result + num

print(result)



names = ["rati","luka","gio","nugo"]
for i in range(0,len(names)):
    print(names[i])