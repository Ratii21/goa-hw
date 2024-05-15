
""" ფუნქციის შექმნა ხდება def - ით, def - ის შემდეგ იწერება ფუნქციის სახელი, 
შემდეგ კი ფრჩხილებში პარამეტრები, რომელსაც ჩვენ ფუნქციას გადავცემთ.
 ეს ყველაფერი დაახლოებით ასე გამოიყურება: def name(პარამეტრი(ები))
 ფქციისთვის პარამეტრის მიწოდება არ არის აუცილებელი """
def greet():
    return "hello!"
print(greet())

def personal_greet(name):
    print("hello", name)
personal_greet("rati")

def doeble_greet(name1,name2):
    print("Hello", name1.capitalize())
    print("Hello", name2.capitalize())
doeble_greet("rati","andria")

""" ფუნქციას შეიძლება ჰქონდეს რამდენიმე output - ი და ჩვენ შეგვიძლია 
 ისინი ერთდროულად ცალცალკე ცვლადებში გავანაწილოთ """
def add_multiple(n1,n2):
    add = n1 + n2
    multiple = n1 * n2

    return add, multiple
   
v1, v2 = add_multiple(2,4)
print(v1)
print(v2)

""" return - ის დაწერის შემდეგ კოდი ითიშება და მის შემდეგ დაწერილ კოდს აღარ კითხულობს """
def add(n1,n2):
    add = n1 + n2
    return add
    multiple = n1 * n2 #<-- ამ კოდს არ კომპიუტერი ღარ წაიკითხავს

""" პითონი საშუალებას აძლევს ფუნქციის არგუმენტებს 
ჰქონდეს ნაგულისხმევი მნიშვნელობები. თუ ფუნქცია გამოიძახება 
არგუმენტის გარეშე, არგუმენტი იღებს თავის ნაგულისხმევ მნიშვნელობას """
def greet1(name = "user"):
    print("Hello",name)
greet1() #გამოიტანს: Hello user - ს
greet1("Rati") #გამოიტანს: Hello Rati - ს