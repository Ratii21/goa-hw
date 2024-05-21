def manual_index(numbers_list, search_value):
#თავდაპირველად def keyword - ის გამოყენებით ვქიმნით ფუნქციას სახელად manual_index
#რომელსაც ფრჩხილებში პარამეტრად გადავცემთ სიას სახელად numbers_lists - ს და ასევე გადავცემთ search_value ცვლადს
    if search_value not in numbers_list:
        return "invalid number"
#შემდეგ if - ის გამოყენებით ვადგენთ პირობას, რომლის მიხედვითაც თუ search_value
#არ არის numbers_list - ში დააბრუნოს სტრინგი: invalid number
    
    for i in range(len(numbers_list)):
        if numbers_list[i] == search_value:
            return i
#შემდეგ for loop - ში range - ის საშუალებით ვქმნით რიცხვთა დიაპაზონს 0 - დან len(numbers_list) - მდე
#ანუ numbers_list - ში ელემენტების რაოდენობებამდე. ამ დიაპაზონში არსებულ ელემენტთა მნიშვნელობას კი 
#საიტერაციო ცვლადი i მიიღებს. ამის შემდეგ for ციკლში if - ის გამოყენებით ვადგენთ შემდეგ პირობას: თუ numbers_list
#ინდექსად i ტოლი იქნება search_value - სი, დააბრუნოს i.
        
print(manual_index([1,2,3,3,4,5],2))
#საბოლოოდ print - ის საშუალებით ვიძახებთ ფუნქციას და არგუმენტებად ვანიჭებთ: სიას, რომელშიც ელემენტებად გვაქვს 1,2,3,3,4 და 5
#და მეორე არგუმენტად ვანიჭებთ 2 - ს.
