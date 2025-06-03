class Student:
    college_name = "ABC College"   #class attribute
    college_address = "123 College St, City, Country"
    college_phone = "123-456-7890"
    college_email = "abc@gmail.com"
    college_website = "www.abccollege.edu"
    college_fax = "123-456-7891"
    college_principal = "Dr. John Doe"
    def __init__(self, name, age, student_id):
        self.name = name  #object attribute
        self.age = age
        self.student_id = student_id

s1 = Student("Alice", 20, "S12345")
print(s1.name, s1.age, s1.student_id, s1.college_name, s1.college_address, s1.college_phone, s1.college_email, s1.college_website, s1.college_fax, s1.college_principal)
s2 = Student("Bob", 22, "S67890")
print(s2.name, s2.age, s2.student_id, s2.college_name, s2.college_address, s2.college_phone, s2.college_email, s2.college_website, s2.college_fax, s2.college_principal)
s3 = Student("Charlie", 21, "S54321")
print(s3.name, s3.age, s3.student_id, s3.college_name, s3.college_address, s3.college_phone, s3.college_email, s3.college_website, s3.college_fax, s3.college_principal)