#class in python

class student:
               #consturctor is a function of class which is called immediately after creating object (automatically)
               def __init__(self, student_name,enr_no,course):
                        self.student_name = student_name
                        self.enr_no = enr_no
                        self.course = course

                def print_details(self):
                        print(f'''name = {self.student_name} enr_no = {self.enr_no } course = {self.course}''')

Yash = student("YASH,0359,"Python")
Aashray = student("AASHRAY,0399,"Java")
Nishant = student("NISHANT,1359,"Javascript")
Parth = student("PARTH,0859,"HTML")
Chetan = student("CHETAN,0346,"CSS")

Yash.print_details()