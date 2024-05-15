""" ლისტის ჩაშენებული ფუნქციები """

""" in-ით ჩვენ შეგვიძლია გავიგოთ არის თუ არა კონკრეტული ელემენტი ცოლექციაში """
cart = ["banana","apple","melon"]
print("melon" in cart)

""" sort() ფუნქცია დაალაგებს რიცხვების სიას ზრდადობით """
numbers = [7, 15, 12, 18, 22]
numbers.sort() 

""" len - ფუნქციით ჩვენ ვითვლით სიაში არსებული ელემენტების რაოდენობას """
names = ["rati","luka","gio","nugo"]
print(len(names))

""" append - ფუნქციით ჩვენ სიის ბოლო ადგილზე ვამატებთ ელემენტს """
nums = [1,2,3,4]
nums.append(5)
print(nums)

""" insert - ფუნქციით ჩვენ ჩვენთვის სასურველ ინდექსზე (რასაც არგუმენტად ვწერთ),
 ვამატებთ ჩვენთვის სასურველ ელემენტს """
nums.insert(1, 1.5)
print(nums)

""" pop - ფუნქციით ჩვენ ვშლით ჩვენთვის სასურველ ელემენტს სიიდან ატრიბუტად 
 სასურველი ელემენტის ინდექსის დაწერით """
nums.pop(1)
print(nums)
