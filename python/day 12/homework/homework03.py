first_side = float(input("enter triangle first side size: "))
second_side = float(input("enter triangle second side size: "))
third_side = float(input("enter triangle third side size: "))
i = 0
while first_side + second_side > third_side and second_side + third_side > first_side and first_side + third_side > second_side and i < 1:
    print("this triangle exists")
    i += 1
else:
    print("try again! this triangle doesn't exists")
    