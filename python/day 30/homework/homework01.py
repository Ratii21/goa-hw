def odd_and_even(list):
    odd = []
    even = []

    for i in range(len(list)):
        if i % 2 == 0:
            even.append(list[i].upper())
        else:
            odd.append(list[i].upper())
    print(odd)
    print(even)

odd_and_even(["rati", "elene", "gio" , "ako" ""])
