#--> match statement == similar to switch case statement

'''day=int(input("Enter the value of the day"))
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday") 
  case _:
    print("No match")'''


#--> match statement == similar to switch case statement

'''day=int(input("Enter the value of the day"))
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday") 
  case _:
    print("No match")'''

# else if statement

'''marks=int(input("Enter your marks"))

if marks>100:
    print("Invalid marks")
elif marks >= 95 and marks <= 100:
    print("You are PASSED with S Grade")
elif marks >=85 and marks < 95:
    print("You are PASSED with A Grade")
elif marks >= 75 and marks < 85:
    print("You are PASSED with B Grade")
elif marks >= 65 and marks < 75:
    print("You are PASSED with C Grade")
elif marks >= 40 and marks < 65:
    print("You are PASSED with P Grade")
elif marks < 40:
    print("You are FAILED")
else:
    print("INVALID MARKS")'''


# for loop in python

'''for i in range (1,101):
    print(i)
for i in range (7,76):
    print(i)
for i in range (6,65):
    print(i)
for i in range (3,1):
    print(i)'''

'''while True:
    x=int(input("Enter the number to print : "))
    if x==0:
        break   #breaks the loop
    print(x)
    print("Enter 0 to break")'''


'''for i in range(1,101):
    if(i%2!=0):          #to print the even numbers
        continue         # continue = skip the ittration 
    print(i)

for i in range(1,101):
    if(i%2==0):          #to print the odd numbers
        continue         # continue = skip the ittration 
    print(i)

for i in range(1,101):
    if(i%2==0):          #to print the odd numbers
        pass         # pass = place holder : no change in code 
    print(i)'''

# Mathematical Operator

'''import math'''

'''print(math.sqrt(144))
print(math.floor(5.9))
print(math.ceil(5.1))'''


'''import random

print(random.randint(1, 7))       #gives the random numbers between the given input
print(random.randrange(1,50))   '''  #give the  

'''import calculator   #importing module

calculator.add(2,5)

calculator.sub(4,5)

calculator.mult(5,5)

calculator.modulas(2,8)

calculator.exp(2,9)


# -> Types of arguments
#when an argument completely depend on position is called positional argument
def greet(student,trainer):
    print(f"GOOD AFTERNOON {trainer}")
    print(f"WELCOME {student}")

#when an argument completely depend on position is called positional argument
greet("Yash","Mohit")                       
#when an argument completely depend on keyword is called keyword argument
greet(trainer="Yash",student="Mohit")     

def print_number(a,b,c):
    print(a)
    print(b)
    print(c)

print_number(1,5,6)


 #-> if we don't know the argument length we use the "variable length arguments" 
def print_number(*args):        #-> this will stored in list
  for i in args:
    print(i)

print_number(1,51,1,5,5,7,63,36,9,6,3,9,6,6,9,8)


 #-> if we don't know the argument length we use the "variable length arguments"
def print_number(**kwargs):      #-> this will stored in dictionaries
  for i in kwargs.keys():
    print(i)
  for i in kwargs.values():
    print(i)
  for k,v in kwargs.items():
    print(f"keys {k} : values {v}")

print_number(Trainers="Govinthan",student1="Yash",student2="Aashray",Grade=True,Marks=9.5)'''


