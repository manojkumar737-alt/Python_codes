def fact_number(a, b):
    i = 1
    while i <= a:
        b *= i
        i += 1
    return b

user_input = int(input("Enter a number to calculate its factorial: "))
result = fact_number(user_input, 1)
print(f"The factorial of {user_input} is {result}")