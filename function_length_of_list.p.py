def length_list(list):
    return len(list)

user_input = input("enter a list of numbers seprated by commas: ")
user_input = user_input.split(',')
list1 = list(map(int, user_input))
result = length_list(list1)
print("The length of the list is:", result)