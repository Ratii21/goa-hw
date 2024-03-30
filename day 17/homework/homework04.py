numbers = [1,2,3,4,5,6,7,8,9,10]

#ჯამი
result = 0

for i in numbers:
    if i % 2 != 0:
        result += i
print(result)

#ნამრავლი
Result = 1

for i in numbers:
    if i % 2 != 0:
        Result *= i
print(Result)
