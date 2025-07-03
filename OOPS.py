#class in python
#--> Constructor

class student:
    # Constructor is a function of class which is called immediately after creating an object (automatically)
    def __init__(self, student_name, enr_no, course):
        self.student_name = student_name
        self.enr_no = enr_no
        self.course = course

    def print_details(self):
        print(f'''name = {self.student_name} enr_no = {self.enr_no} course = {self.course}''')

# Corrected: Enrollment numbers are now strings
Yash = student("YASH", "0359", "Python")
Aashray = student("AASHRAY", "0399", "Java")
Nishant = student("NISHANT", "1359", "Javascript")
Parth = student("PARTH", "0859", "HTML")   # Changed to string
Chetan = student("CHETAN", "0346", "CSS")  # Changed to string

Yash.print_details()
Aashray.print_details()
Nishant.print_details()
Parth.print_details()
Parth.print_details()



class laptop(student):          #the features of student class has been passed down to laptop class 
        def __init__(self,studend_name,enr_no,course,cpu,gpu,ram):
                super().__init__(studend_name,enr_no,course)
                self.cpu=cpu
                self.gpu=gpu
                self.ram=ram
        def print_details(self):
                print(f"CPU = {self.cpu} GPU = {self.gpu} RAM = {self.ram}")
                return super().print_details()


acer=laptop("Mohit",1234,"Python","i7",12,"13650 HX")
acer.print_details()

# -->Polymorphism

class Bird:
    def sound(self):
        print("Chirp")

class Cat:
    def sound(self):
        print("Meow")

# Define make_sound function outside of the classes
def make_sound(animal):
    animal.sound()

# Create instances of Bird and Cat
b = Bird()
c = Cat()

# Call make_sound with the instances
make_sound(b)  # Prints: Chirp
make_sound(c)  # Prints: Meow

#--> METHOD OVERWRITING

class Parent:
   def show(self):
      print("Parent's Method")  

class Child:
   def show(self):
      print("Child's Method")

obj = Parent()
obj.show()
obj = Child()
obj.show()

# -->OPERATOR OVERLOADING

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)
p1=Point(1,2)
p2=Point(3,4)
p3=p1 + p2
print(p3.x,p3.y) 

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __sub__(self,other):
        return Point(self.x - other.x, self.y - other.y)
p1=Point(1,2)
p2=Point(3,4)
p3=p1 - p2
print(p3.x,p3.y) 

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __mul__(self,other):
        return Point(self.x * other.x, self.y * other.y)
p1=Point(1,2)
p2=Point(3,4)
p3=p1 * p2
print(p3.x,p3.y) 

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __truediv__(self,other):
        return Point(self.x / other.x, self.y / other.y)
p1 = Point(1,2)
p2 = Point(3,4)
p3 = p1 / p2
print(p3.x,p3.y) 


# --> Exception Handling in python

#-> TRY EXCEPT BLOCK
try:
    print(1/0)
    print(int,{"Hello"})

except:
    print("Thre is an error")
print("rest of the program")



try:
    print(1/0)
    print(int,{"Hello"})

except ZeroDivisionError:
    print("We cannot divide by zero, try another number")

except ValueError:
    print("Cannot convert this string to number") 
print("rest of the program")


# -> USING ELSE BLOCK

try:
    result = 10/2

except ZeroDivisionError:
    print("Error !!")
    
else:
    print("Success.",result)


# -> RAISING EXCEPTIONS MANUALLY

age=int(input("Enter your age : "))

if age < 18:
   raise ValueError("Age must be 18 or older.")

else:
    print("Access granted. 👍")




# File Handling

#f=open("firstfile.txt","x")   # x = create
'''r=open("firstfile.txt","r")    # r = read the file 

content=r.read()
r.close()
print(content)
'''

f=open("File2.txt","a")  #Creates a file if file does not exist
f.write("Kai pAn This is new content ")
f.close()

# If we try to create a file which does not exist it will create the new file

try:
    r=open("File3.txt","r")
    content=r.read()
    r.close()
    print(content)

except FileNotFoundError:
    print("The file is not there!! ⪥")


# FILE CHECK AND MANAGEMENT (USING OS MODEULE)

import os

print(os.path.exists("File2.txt"))      #Check weather file exists in the path or not

# os.remove("firstfile.txt")            #deletes the given file

# os.rename("calculator.py","Calc.py")    #this will change the file name


with open("download.jpg","rb") as f:
    content=f.read()

    print(content)

    with open("copy_F1.jpg","wb") as f:
        f.write(content)
         
with open("filereadandwrite")