user_inputs = input("enter numbers with space seprated for check palindrome or not")
list1 = list(map(int, user_inputs.split()))
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print(list1, "is palindrome")
else:
    print(list1,"no palindrome")