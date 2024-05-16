def filter(list):
    result = []

    for i in list:
        if len(i) % 2 == 0:
            result.append(i.upper())
        else:
            result.append(i.capitalize())
    return result

print(filter(["goa_best" , "vano" , "nesvi" , "tskhVarAdzE"]))
