numbers = [1,2,3,4,5,6,7,8,9,10]

#sum
sum_of_the_even_numbers = 0

for i in numbers:
    if i % 2 != 0:
        sum_of_the_even_numbers += i
print(sum_of_the_even_numbers)

#multipied
Multiplied_of_the_even_numbers = 1

for i in numbers:
    if i % 2 != 0:
        Multiplied_of_the_even_numbers *= i
print(Multiplied_of_the_even_numbers)

