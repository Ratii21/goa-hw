def low_up(list):
    new_list = []
    for i in list:
        if i.isupper() == True:
            new_list.append(i.lower())
        elif i.islower() == True:
            new_list.append(i.upper())
    return new_list
print(low_up(["vano" , "DAVIT" , "LUKA" , "nika"]))