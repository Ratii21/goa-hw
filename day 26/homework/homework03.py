def capital_letter(words):
    
    new_list = []
    
    for i in range(0,len(words)):
        new_list.append((words[i].title()) or (words[i].capitalize()))
    
    return(new_list)

print(capital_letter(["david", "chad", "gigachad"]))

