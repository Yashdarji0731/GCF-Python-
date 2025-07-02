def greet(a):     #a -> parameters
    print("Hello World\n" + a) #function defination

greet("Yash") #function calling #Yash -> argument

#Addition
def add(a,b):
    print(a+b)

add(5,5)

#Subtraction
def sub(a,b):
    print(a-b)

sub(5,5)

#Mutiplication
def multi(a,b):
    print(a*b)

multi(5,5)

#Division
def div(a,b):
    print(a/b)

div(5,5)

#Exponential
def expo(a,b):
    print(a**b)

expo(5,5)

#Modules
def modules(a,b):
    print(a%b)

modules(5,5)

# --> returning functions

#Addition
def add(a,b):
    return(a+b)

add(5,5)

#Subtraction
def sub(a,b):
    return(a-b)

sub(5,5)

#Mutiplication
def multi(a,b):
    return(a*b)

multi(5,5)

#Division
def div(a,b):
    return(a/b)

div(5,5)

#Exponential
def expo(a,b):
    return(a**b)

expo(5,5)

#Modules
def modules(a,b):
    return(a%b)

modules(5,5)

#Addition
def add(a,b):
    return(a+b)

print(add(5,5)+add(1,3))

add(5,5)

# name="YASH"

# def add(a,b):
#     print(name)
#     studend="Yash"
#     return a+b

# print(name)
# print(student)

# -->  Duplicate Values 
a=10
b="string"
c=True
d=1.2250
print(type(a))  #type() -> returns the datatype of the variable
print(type(b))
print(type(c))
print(type(d))

# -> Symbol of list is []

e=[1,2,3,"abc",True,1.2503]
print(type(e))
print(e)

# -> print index

e=[1,2,3,"abc",True,1.2503]
#  0 1 2   3     4     5
print(type(e))
print(e[2])
print(e[3])

# -> modifying elements in array

e=[1,2,3,"abc",True,1.2503]
#  0 1 2   3     4     5
print(type(e))
print(e)
e[2]="two"  #modify elements
print(e)
print(e[-3])

# -> Append() = adds the element at last position

e=[1,2,3,"abc",True,1.2503]
#  0 1 2   3     4     5
print(e)
e.append(1000) #adds the element at last postion of the list
print(e)

# -> Index()

e=[1,2,3,"abc",True,1.2503]
#  0 1 2   3     4     5
print(e)
print(e.index(2))

# -> Extend() = combining the two lists

e=[1,2,3,"abc",True,1.2503]
f=[25,17,7]
#  0 1 2   3     4     5
print(e)
e.extend(f) #extend = the argument should be list = f is a list
print(e)

# -> remove() = remove the same elements in the list

e=[1,2,3,"abc",True,1.2503]
f=[25,17,7,65,85,7,69,35,7]
#  0 1 2   3     4     5
print(e)
e.extend(f)
print(e)
e.remove(7)
print(e)

# -> pop() = pops out our last element

e=[1,2,3,"abc",True,1.2503]
f=[25,17,7,65,85,7,69,35,7]
#  0 1 2   3     4     5
print(e)
e.extend(f)
print(e)
e.remove(7)
print(e)
e.pop(1) #pop = by default remove the last element ,pop(element) = removes the element at argument position
print(e)

# -> clear() = clears all the values
e=[1,2,3,"abc",True,1.2503]
f=[25,17,7,65,85,7,69,35,7]
#  0 1 2   3     4     5
print(e)
e.extend(f)
print(e)
e.remove(7)
print(e)
e.pop(1)
print(e)
e.clear()
print(e)

# symbol of slice : 

e=[1,2,3,"abc",True,1.2503]
#  0 1 2   3     4     5

#print(e[1:])  slicing -> [start:stop-1]
print(e[:4])

# reverse

e=[1,2,3,"abc",True,1.2503]
#  0 1 2   3     4     5

e.reverse()

#Defination of print and return
#print -> give value inside the function
#return -> give value by calling the function
def greet():
    print("hi")
    return 1000

print(greet()+1) #1000

# sort = orders the elements in ascending order

e=[1,2,3,"abc",True,1.2503]
#  0 1 2   3     4     5
f=[25,17,7,65,85,7,69,35,7]
e.reverse()
print(e)
f.sort()
print(f)

# reassigning the values

e=[1,2,3,"abc",True,1.2503]
f=e
f.pop()
print(f)
print(e)

#copy -> creating duplicates

e=[1,2,3,"abc",True,1.2503]
f=e.copy() #creating duplicates
f.pop()
print(f)
print(e)

# -> insert = insert the value between the array through index no and updated values
#             inserts the specified value at the specified position 
e=[1,2,3,"abc",True,1.2503]
f=e
f.pop()
print(f)
print(e) 
e.insert(2,6)  #insert(index no., value)
print(e)


#--> Tuples in python 

a=(1,23,3,5,7,5,)
print(a)
print(type[a])
print(a[1]) #tuples = accessed by index
print(a[5]) #tuples = accessed by index

# The len() function returns the number of items in an object.

a=(1,23,3,5,7,5,)
b=(1,5,3,8,66,8)

print(len(a))
print(a+b)  #Adding two tuples
print(b*3)  #give the same tuple 3 times 

a=(1,23,3,5,7,5,)
b=(1,5,3,8,66,8)

print(len(a))
print(a+b)
print(b*3)
print(b.count(3))  #counts the number of times elements repeated in the tuple
print(b.index(3))  #retrieves the index of the given element at first occuranse