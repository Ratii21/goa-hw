def squared_list(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i ** 2)
    return new_lst
print(squared_list([1,2,3,4,5]))
