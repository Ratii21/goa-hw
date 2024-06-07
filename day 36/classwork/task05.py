def human_years_cat_years_dog_years(human_years):
    catyears = 0
    dogyears = 0
    
    for i in range(1,human_years + 1):
        if i == 1:
            catyears += 15
            dogyears += 15
            
        elif i == 2:
            catyears +=  9
            dogyears +=  9
            
        elif i > 2:
            catyears += 4 
            dogyears += 5 
    
    return [human_years,catyears,dogyears]