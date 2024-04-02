surname = "Tikurishvili"
result = ""

for i in range(0,len(surname)):
    if i % 2 == 0:
        result += surname[i]

print(result)