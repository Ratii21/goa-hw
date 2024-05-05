password = ("rati123456")
user_guess = input("what is the password: ")

i=1

while password != user_guess and i <= 5:
    print("try again! you are on guess" ,i, )
    user_guess = input("what is the password: ")
    i += 1
if i == 6:
    print("system blocked")
    i += 1
if password == user_guess:
    print("congrats")
    
