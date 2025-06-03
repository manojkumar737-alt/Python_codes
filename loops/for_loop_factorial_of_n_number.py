user_input = int(input("enter the number for factoral: "))
min  = 1
factorial_result = 1
for i in range(min, user_input + 1):
    factorial_result = factorial_result * i
print(f"The factorial of {user_input} is {factorial_result}")