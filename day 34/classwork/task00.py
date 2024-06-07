def even(num_list):
    new_list = []
    for i in num_list:
        if i % 2 == 0:
            new_list.append(i)
    return len(new_list)
print(even([1,2,3,4,5,6,7,8,9,10]))