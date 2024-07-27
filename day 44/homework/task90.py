def rev(num):
    num = str(num)
    rev_num = ""
    count = len(num) - 1
    while count >= 0:
        rev_num += num[count]
        count -= 1
    print(int(rev_num))


rev(12345)