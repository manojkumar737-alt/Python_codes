num = 1
i = 0
list = []
while num <= 10:
    num1 = num * num
    print("number: ", num1)
    list.append(num1)
    num += 1
#print(list)
tup = tuple(list)
user_input = int(input("Enter a number to search in the tuple: "))
if user_input in tup:
        print(f"{user_input} is present in the tuple.")
else:
        print(f"{user_input} is not present in tye tuple.")
while i < len(tup):
    if tup[i] == user_input:
        print(f"Index of {user_input} in the tuple is: {i}")
        i += 1
    else:
        i += 1