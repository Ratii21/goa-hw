""" slice - ჩამოჭრა """
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[1:5])

""" ასევე შეგვძლია ჩვენ მხოლოდ საწყისი ინდექსის არჩევა 
 რის შემდეგაც დანარჩენს თვითონ ჩამოაჭრის"""
print(numbers[1:])

""" ასევე შეგვძლია ჩვენ მხოლოდ საბოლოო ინდექსის არჩევა 
 რის შემდეგაც არჩეულ ინდექსამდე ყველა ელემენტი ჩამოიჭრება """
print(numbers[:4])



vehicle = 'motorbike'
print(vehicle[:])



""" ასევე შეიძლება გვქონდეს უარყოფითი ინდექსები, სადაც შეიძლება
 რომ მინუსის ნიშანს მნიშვნელობად უბრალოდ "ბოლოდან" ჰქონდეს 
 ანუ მაგალითად ელემენტი ინდეხსად "-1" ეს იგივეა რაც ელემენტი "ბოლოდან 1" """

print(numbers[-1])
print(numbers[:-1])
