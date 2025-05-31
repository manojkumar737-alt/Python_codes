user_list1 = input("Enter the first list of numbers separated by spaces: ")
user_list2 = input("Enter the second list of numbers separated by spaces: ")
list1 = list(map(int, user_list1.split()))
list2 = list(map(int, user_list2.split()))

def print_list_in_line(list1, list2, list3=[]):
    list3 = list1 + list2
    for i in list3:
        print(i, end=' ')
    print()  # To ensure the output ends with a newline 
print_list_in_line(list1, list2, list3=[])
def add_element_to_list(list1, list2, list3=[]):
    list3 = [a + b for a, b in zip(list1, list2)]
    print(list3)
add_element_to_list(list1, list2, list3=[])




        