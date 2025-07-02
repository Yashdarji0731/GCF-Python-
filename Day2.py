#sets in python 
#Not ordered(no index value), partially mutable(modified by methods)
#unique elements (they dont allow duplicates)

b={1,2,3,4,5,6}
c={1,1,2,3,7,1,12,844,7,55,7,51,5754,774,2,21,1}
print(c)
print(b)
print(type(b))

# -> Add

c={1,1,2,3,7,1,12,844,7,55,7,51,5754,774,2,21,1}
print(c)
c.add("add") #adds the element in the set
print(c)

# -> Remove

c={1,1,2,3,7,1,12,844,7,55,7,51,5754,774,2,21,1}
print(c)
c.add("add") #adds the element in the set
print(c)
c.remove("add") #removes the element from the set

c={1,1,2,3,7,1,12,844,7,55,7,51,5754,774,2,21,1}
print(c)
c.add("add") #adds the element in the set
print(c)
c.remove("add") #removes the element from the set
# c.remove("add") #-->key error :- removing the same element from the set
c.discard("add")  

# -> Empty set 

emset=set() #creating empty set
print(emset)
print(c)

# -> Boolean method

c={1,2,85,285,52254,2,50,25,0,24,14,22,41,24,25,50,7}
print(c)
print(10 in c) #if the value is present in the set then output is true else false

# -> update
b={5,5,25,45,4,2,5,1,5532,65,54}
c={1,2,85,285,52254}
print(c)
c.update(b) # adds a set in the set(UPDATES MULTIPLE ELEMENTS)
print(c)

# -> clear

c={1,2,85,285,52254}
print(c)
c.clear() # clears out all the elements in the sets 
print(c)

# -> Copy

b={1,2,85,285,52254}
e=b.copy()  # creates a duplicate copy of the element
print(e)

#union(|) = combines both set and duplicates will be considered as single value

A = {1, 2, 3, 4}
B = {5, 6, 7, 8}
#Two methods to print the element

print(A.union(B))
print(A|B)

#Intersection(&) = elements which are present in A and B (Common elements)

A = {1, 2, 7, 4}
B = {5, 6, 7, 8}
#Two methods to print the element
print(A.intersection(B))
print(A&B)



A = {1, 2, 3, 4}
B = {5, 6, 7, 8}
#Two methods to print the element
print(A.difference(b)) #Elements which are in "A" but not in "B"
print(A-B)

A = {1, 2, 3, 4}
B = {5, 6, 7, 8}
#Two methods to print the element
print(B.difference(A)) #Elements which are in "B" but not in "A"
print(B-A)

A = {1, 2, 7, 4}
B = {5, 6, 7, 8}
#Two methods to print the element
print(A.symmetric_difference(B)) #symmetric_difference(^) = elements which are not in "A" and "B"
print(A^B)

#Frozen set after created a set, changing the value or update the value in not possible

x=frozenset([1,2,3,4,5,6]) #immutable even via methods
print(x)  #->Attribute error
x.add(7)

#--> Dictionary ={key : value, key : value, key : value}
# unorderd , cannot have duplicates in key
# mutable
# Fast lookups using keys
#python dictionary -> '' or ""
#json -> ""

y={'Name':"Yash","age":"18","Subject":"Python","istrainer":True}
print(type(y))
print(y)
    

  a={'name':"Vishal","age":"25","subject":"python","istrainer":True,"other_trainer":{"name":"Shivam","age":"20",}}
 c={"name":"Sandeep"}
 print(a)
 print(type(a))
 print(a['name'])
 print(a["subject"])
 a["name"]="Sahil"
 a["istrainer"]="False"
 print(a)
 print(a["other_trainer"])
 a.update(c)
 print(a)


for i in a.values():
    print(i)

for k,v in a.items():
    print("key = "+k)
    print("value = " +str(v))


string in python
