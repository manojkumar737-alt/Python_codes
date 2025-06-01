try:
    with open("number.txt", "w") as file:
        file.write("1,2,45,55,86,76")
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")
try:
    with open("number.txt", "r") as file:
        content = file.read()
        numbers = [int(num) for num in content.split(",") if int(num) % 2 != 0]
        print(numbers)
        print("Sum of odd numbers:", sum(numbers))
except IOError as e:
    print(f"An error occurred while reading the file: {e}")
