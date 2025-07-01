a={'name':"Yash", 'Age':18, 'Subject':"Python", 'isstudent': True}
print(type(a))
print(a['name'])
print(a['Subject'])
a['name']="YASH"
a['isstudent']=False
print(a)


a={'name':"Yash", 'Age':18, 'Subject':"Python", 'other_student':{'name':"Mohit", 'Age':18, 'isstudent':True}}
print(a['other_student']['name'])
print(a['other_student']['Age'])
print(a['other_student']['isstudent'])
c={'name':"Mohit", 'Age':"18",'cource':"Python"}
a.update(c) #updates the values by keys if there is no key then appends the entire key pairs
print(a)

a={'name':"Yash", 'Age':"18", 'Subject':"Python", 'other_student':{'name':"Mohit", 'Age':"18", 'isstudent':True}}
print(a['other_student']['name'])
print(a['other_student']['Age'])
print(a['other_student']['isstudent'])
c={'name':"Mohit", 'Age':"18",'cource':"Python"}

for i in a.keys():    #print the keys from the sets
    print(i)  
for i in a.values():  #print the values from the sets
    print(i)


for k,v in a.items(): #print the key and values from the set
    print("key=" +k)
    print("value=" +str(v))

#--> Strings in Python
# -> Multiline strings

a='''GOOD MORNING
GOOD AFTERNOON
GOOD EVENING'''
B="ABCDEFGHIJKLMNOPQRSTUVWZ"
print(a)
print(B[5])     #accessing string via character
print(B[-4])    #-ve values print it in reverse values
print(B[3:6])   #slice :- gives the neccesary elements from the string [start:stop-1]
print(B[9:])
print(B[15:20])
print(B[-9:-4])

# -> String methods

a="ABCDEFGHIJKLMNOPQRSTUVWZ"
b="abc"
print(a.lower())                #change the string in lower case
print(a.upper())                #change the string in upper case
print(a.strip())                #remove the elements at start and end
print(a.strip()+b)              #remove the elements at start and end and add the second string  
print(a.replace("A","a"))       #replace the string with given value
print(a.replace("ABC","123"))   #replace the string with given value

a="A B C D E F G H I J K L M N O P S J I T Y Q N"
b="abc"
c=a.split(" ")                  #converts the string into list

print("=".join(c))              #converts the list into string

a="A B C D E F G H I J K L M N O P S J I T Y Q N"
b="abc"
c=a+b
print(c.count("N"))                  #count = number of times the given string repeated in the original string
print(c.startswith("A B C D"))       #checking the string if the given value is match with the string it gives "True"
print(c.endswith("A B C D"))         #checking the string if the given value is not match with the string it gives "False"
print(b*3)                           #Multiplied the string
print("N" in a)

'''a=int(input("Enter the number A ="))   #input from the user (default inout takes it as string)
b=int(input("Enter the number B ="))
print("The addition is ",{a+b})
print("The subtraction is ",{a-b})
print(f"The multiplication is {a*b}")  #string formating
print(f"The division is {a/b}")
print(f"The modulas is {a%b}")
print(f"The exponential is {a**b}")
'''

# -> EMAIL VALIDATOR

'''email=input("Enter your email:")
if "@" in email and email.endswith(".com"):
    print("Valid email")
else:
    print("Invalid email")'''

'''age=int(input("Enter your Age :"))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")'''

marks=int(input("Enter your marks :"))
if marks >= 35:
    print("You passed !")
else:
    print("You failed")