""" სტრინგის ჩაშენებული ფუნქციები """

""" სტრინგებზე ფუნქციების გამოყენების სტრუქტურა: 
"string".function(არგუმენტი(თუ სჭირდება ფუნქციას)) """

""" upper - ამ ფუნქციით სტრინგის ყოველი ასო გახდება დიდი"""
print("name".upper())

"""lower - ამ ფუნქციით სტრინგის ყოველი ასო გახდება პატარა"""
print("NAME".lower())

""" capitalize - ამ ფუნქციით სტრინგის პირველი ასო გახდება დიდი"""
print("name".capitalize())

""" title - ამ ფუნქციით სტრინგში ყველა ასო რომლის წანაც წერია "space"
 გახდება დიდი """
print("my name is rati".title())

""" isupper - ამ ფუნქციით ვამოწმებთ არის თუ არა სტრინგში არსებულია ყველა ასო  
 დიდია თუ პატარა. თუ დიდია ყველა ასო დააბრუნებს True - ს, ხოლო სხვა შემთხვევაში დააბრუნებს False - ს"""
print("NIKA".isupper())

""" islower - ამ ფუნქციით ვამოწმებთ არის თუ არა სტრინგში არსებულია ყველა ასო  
 დიდია თუ პატარა. თუ პატარაა ყველა ასო დააბრუნებს True - ს, ხოლო სხვა შემთხვევაში დააბრუნებს False - ს """

""" find ფუნქციით ჩვენ ვპოულობთ ატრიბუტად მოცემული სტრინგის ინდექსს სტრინგში"""
print("andria".find("a")) 
""" ზემო შემთხვევაში ხედავთ, "a" - არგუმენტი სტრინგში ორჯერ გვაქვს თუმცა
 find ფუნქცია მხოლოდ პირველად რომელიც შეხვდება იმის ინდექსს გამოიტანს.
 ასევე თუ მოცემული არგუმენტი სტრინგში არ მოიძებნა ფუნქცია -1 - ს დააბრუნებს"""


