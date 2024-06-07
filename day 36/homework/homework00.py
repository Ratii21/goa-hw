def abbrev_name(name):
    new_name = name.title() 
    first_name = new_name[0]
    second_name = new_name[(new_name.find(" ")) + 1]
    return first_name + "." + second_name
