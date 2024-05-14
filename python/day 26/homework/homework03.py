def capital_letter(words):
    
    new_list = []
    
    for i in words:
        new_list.append(i.capitalize())
    
    return(new_list)

print(capital_letter(["david", "chad", "gigachad"]))

