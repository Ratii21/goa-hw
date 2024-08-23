def dna_to_rna(dna):
    rna = ""
    for i in dna:
        if i != "T":
            rna += i
        else: 
            rna += "U"
    return rna