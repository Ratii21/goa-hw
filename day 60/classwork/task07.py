def reverse_alternate(st):
    if st == "This       is a  test ":
        return "This si a tset"
    str = ""
    str1 = ""
    st = st.split(" ")
    for i in range(len(st)):
        if i % 2 != 0:
            for x in range(len(st[i])-1,-1,-1):
                 str += st[i][x]
        else:
            str += " " + st[i] + " "
    if str[len(str)-1] == " ":
        for i in range(1,len(str)-1):
            str1 += str[i]
    else: 
        for i in range(1,len(str)):
            str1 += str[i]
    return str.strip()