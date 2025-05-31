def read_file(file_path):
    try:
        print("before changing the file content")
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:\n", content)
        with open(file_path, 'a') as file:
            # Appending new content to the file
            file.write("\n")
            file.write("My name is Manoj Kumar.\n")
            file.write("I have 12 years expierence in shell scrtipting.")
        print("File content changed successfully.")
        with open(file_path, 'r') as file:
            updated_content = file.read()
            print("Updated file content:\n", updated_content)
    except IOError as e:
        print(f"Error reading or writing the file: {e}")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You don't have permission to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Execution completed.")

# Example usage
file_path = "test_file.txt"
read_file(file_path)