word = "Manoj"
with open("file_test.txt", "r") as file:
    data = file.read()
if word in data:
    print(f"{word} is present in the file.")
else:
    print(f"{word} is not present in the file.")
