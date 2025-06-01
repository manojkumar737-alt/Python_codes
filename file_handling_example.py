try:
    with open("test2_file.txt", "x") as file:
        file.write("Hello, this is a test file.\n")
        file.write("This file is created to demonstrate file handling in Python.\n")
        file.write("We are using the 'xt' mode to create a new file.\n")
        file.seek(0)  # Move the cursor to the beginning of the file
        file.close()
    with open("test2_file.txt", "r") as file:
        # Read the contents of the file
        print("File created successfully. Reading contents:")
        file.seek(0)
        data = file.read()
        print(data)
        file.close()
except FileExistsError:
    print("File already exists. Please choose a different filename.")
except Exception as e:
    print(f"An error occurred: {e}")
# This code attempts to create a new file and write some text into it.