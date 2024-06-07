def manual_counter(num_list, element):
    counter = 0
    for i in num_list:
        if i == element:
            counter += 1
    return counter
print(manual_counter([1,2,3,4,3,5], 3))