#example
user_input = int(input("please enter number between 1-10: "))
if user_input == 5:
    print("you won!")

else:
    print("you lost!")



#ლოგიკური ოპერატორები

""" and """

print(True and False) - ''' გამოიტანს False '''
print(True and True) - ''' გამოიტანს True '''
print(False and False) - ''' გამოიტანს False '''
 
is_boy = True
is_14 = False

if is_boy and is_14:
    print("you won!")
else:
    print("you lost!")

""" or """

print(True or False) - ''' გამოიტანს True '''
print(False or False) - ''' გამოიტანს False '''
print(True or True) - ''' გამოიტანს True '''

if is_boy or is_14:
    print("you won!")
else:
    print("you lost!")

#შევამოწმოთ ლუწობა და კენტობა
    
print(5 % 2 == 0) - '''ამ შემთხვევაში იქნება False  ანუ კენტია'''
print(6 % 2 == 0) - '''ამ შემთხვევაში იქნება True ანუ ლუწია'''


