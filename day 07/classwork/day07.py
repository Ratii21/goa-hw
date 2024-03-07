#classwork

#1
name = input("enter you name :")
surname = input("enter your surname :")
age = input("enter your age :")
print(name)
print(surname)
print(age)

#2
num1 = int(input("enter any number :"))
num2 = int(input("enter any number :"))

print(num1 > num2)
print(num1 < num2)
print(num1 == num2)

#data type

print(type(6))
print(type("rati"))
print(type(5.6))
print(type("6"))

''' ფუნქციები რომლებიც ერთი მონაცემთა ტიპიდან გადაყვათ მეორეში 
ამ შემთხვევაში int(),str() და float() ქვიათ მექანიკური მონაცემთა ტიპის შეცვლა
მექანიკურში ვგულისხმობ იმას რომ ჩვენ ჩვენი ხელით გარდავქმნით ერთი ტიპიდან მეორეში'''

# int() ეს ფუნქცია გვეხმარება იმაში რომ მნიშვნელობა გარდავქმნათ ინტეჯერად ანუ მთელ რიცხვად.
print(int(5.9))
print(int("5") + 5)

# float() ეს ფუნქცია გვეხმარება იმაში რომ მნიშვნელობა გარდავქმნათ ათწილად რიცხვად.
print(float("5.6"))
print(float(3))

# str() ეს ფუნქცია გვეხმარება იმაში რომ ნებისმიერი მნიშვნელობა გარდავქმნათ სტრინგად.
print(str(5) + "5")
print(str(3.4) + "1")

# type() ეს ფუნქცია გვეხმარება იმაში რომ გავიგოთ კონკრეტული მნიშვნელობა რა ტიპის არის.
print(type(3.1))
print(type(5))
print(type("luka"))
