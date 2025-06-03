def search_word_in_file():
    file_path = input("Enter the path of the file: ")
    word_to_search = input("Enter the word to search for: ")

    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if word_to_search in line:
                    print(f"Line {line_number}: {line.strip()}\n")
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
search_word_in_file()

def search_word_in_file_with_line_numbers():
    file_path = input("Enter the path of the file: ")
    word_to_search = input("Enter the word to search for: ")

    try:
        line_number = 1
        with open(file_path, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                if word_to_search in line:
                    print(f"\n Found '{word_to_search}' in line no : {line_number}: {line.strip()}")
                line_number += 1
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
search_word_in_file_with_line_numbers()