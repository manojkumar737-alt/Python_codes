marks = int(input("marks: "))
if (marks >= 90):
    print("pass with grade A, and total marks is ", marks)
elif(marks >=80 and marks <90):
    print("pass with grade B, and total marks is ", marks)
elif(marks >=70 and marks < 80):
    print("pass with grade C, and total marks is ", marks)
else:
    print("student failed, marks less then ", marks)