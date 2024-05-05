def avarage(start,end):
    list = []
    sum = 0
    for i in range(start,end):
        sum += i
        list.append(i)
    print(sum/len(list))
avarage(1,10)

    