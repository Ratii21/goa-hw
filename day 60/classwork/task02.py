def is_pangram(st):
    st = st.lower()
    al = "abcdefghijklmnopqrstvwxyz"
    for i in al:
        if i not in st:
            return False
    return True