try:
    with open("file_test.txt", "w") as f:
        f.write("My name is manoj Kumar\n")
        f.write("I am a Software Engineer\n")
        f.write("I am from India\n")
        print("File created successfully.")
    with open("file_test.txt", "r") as f:
        content = f.read()
        print("File content:")
        print(content)
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")
finally:
    print("Execution completed.")
    with open("file_test.txt", "r") as f:
        content = f.read()
        new_content = content.replace("manoj Kumar", "Manoj Kumar")
        print("\n Updated content:")
        print(new_content)
    with open("file_test.txt", "w") as f:
        f.write(new_content)
    print("File updated successfully.")
    with open("file_test.txt", "r") as f:
        content = f.read()
        print("\nFinal content of the file:")
        print(content)