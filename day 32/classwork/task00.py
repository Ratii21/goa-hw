

def manual_index(n_list, s_value):
    if s_value not in n_list:
        return "invalid number"
    
    for i in range(len(n_list)):
        if n_list[i] == s_value:
            return i
        
print(manual_index([1,2,3,3,4,5],2))


