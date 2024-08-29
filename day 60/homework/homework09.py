def DNA_strand(dna):
    str = ""
    for i in dna:
        if i == "A":
            str += "T"
        elif i == "T":
            str += "A"
        elif i == "G":
            str += "C"
        elif i == "C":
            str += "G"
    return str