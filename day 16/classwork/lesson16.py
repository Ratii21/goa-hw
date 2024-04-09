''' list '''


cars = ["BMW", "Mercedes", "Ferrari", "Honda", "Toyota", "Nissan"]
print(cars[1])
print(cars[0])
print(cars[3])


name = ["Rati", "Bandelidze"]
print(name[0], name[1])


age = int(input("enter your age: "))
mail = input("enter your mail: ")
user = [age, mail]
print(user[0], user[1])


#list-ში შეგვიძლია ნებისმიერი data type-ს შენახვა

#string - იც ჩვეულებრივი ცოლექციაა
luka = "name"
print(luka[1])

# " . " - dot
# " , " - comma

#ჩვენ შეგვიძლია შევქმნათ ცვლადი ინდექსების საშუალებით
Rati = name[0]


#ჩვენ შეგვიძლია list - ში ინდექსის საშუალებით ელემენტის შეცვლა
films = ["harry potter", "fast and furious", 5, 6.9]
films[2] = "GOA"
print(films)