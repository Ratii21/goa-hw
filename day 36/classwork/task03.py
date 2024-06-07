
def get_even_numbers(arr):
    new_list = []
    for i in arr:
        if i % 2 == 0:
            new_list.append(i)
    return new_list