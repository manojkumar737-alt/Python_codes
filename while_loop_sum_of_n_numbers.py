i = 1
user_input = int(input("enter the range of number to need to sum: "))
sum = 0
while i <= user_input:
    sum = sum + i
    i += 1
print("The sum of the first", user_input, "numbers is:", sum)