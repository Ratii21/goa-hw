def index_of_element(lst,x):
    
    for i in range(0,len(lst)):
        if x == lst[i]:
            return i
print(index_of_element([1,2,3,4,5], 2))