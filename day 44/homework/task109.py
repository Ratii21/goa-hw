def largest(lst):
    lst.sort()
    return lst[len(lst)-1]

print(largest([1,2,3,9,5,2]))