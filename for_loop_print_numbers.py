min = 1
max = 5
list = []
for i in range(min, max +1):

    j = i * i
    print(f"the square of {i} is {j}")
    list.append(j)
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
    print("------------")
print("the list of square is : ", list)
tup = tuple(list)
x = input("enter the number to check if it is in the tuple: ")
if int(x) in tup:
    print(f"{x} is in the tuple")
else:
    print(f"{x} is not in the tuple")
print("the tuyple is : ", tup)