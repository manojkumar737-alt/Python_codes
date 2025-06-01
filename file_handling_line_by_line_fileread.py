try:
    with open("test1_file.txt", "r") as file:
        line1 = file.readline()
        print("First line of the file:", line1.strip())
        file.seek(0)
        line2 = file.readline()
        print("Second line of the file:", line2.strip())
        line3 = file.readline()
        print("Third line of the file:", line3.strip())
        file.close()
    with open("test1_file.txt", "r") as file:
        data = file.read()
        print("\nContents of the file:")
        print(data)
        file.close()
        print("File closed successfully.")  
except FileNotFoundError:
    print("Error: The file 'test1_file.txt' does not exist.")
except Exception as e:
    print("An unexpected error occurred:", str(e))