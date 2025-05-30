def largest_number (numbers, pos):
    top = sorted(numbers, reverse=True)[:pos]
    return top
user_input = input(" Enter numbers seprated with space: ")
pos = int(input("enter witch postion of number you want: "))
pos1 = pos-1
numbers = list(map(int, user_input.split()))
result = largest_number(numbers, pos)
print("largest number is: ", result[pos1])