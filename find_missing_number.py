user_input = input("please enter number with space seprated: ")
numbers = list(map(int, user_input.split()))
min = numbers[0]
max = numbers[-1]
exp_set = set(range(min, max+1))
act_set = set(numbers)
missing = exp_set - act_set
print("Missing number are : ", list(missing))