def word_search(query, seq):
    list = []
    for i in seq:
        if query.lower() in i.lower():
            list.append(i)
    if list == []:
        list = ["None"]
    return list
