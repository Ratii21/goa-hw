def func(num_list):
    sum = 0
    for i in num_list:
        if i % 4 == 0:
            sum += i
    return sum
print(func([1,2,3,4,5,6,7,8]))