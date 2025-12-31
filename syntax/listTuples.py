#list 

x = [4 , "hello" , True]

print(len(x)) #tells length of list ,works for string too

x.append("hello") #add this to our list

x.extend([4,5,6,7,8]) #add this to our list

print(x.pop()) #remove and return the last element in the list

#we can also do x.pop(0) to remove 1st element

#list are mutable

#list comprehension -> l = [j for j in range(1,11)] -> its a concise way to create lists in python 

#eg: 
squares = [x**2 for x in range(1,11)]
print(squares)

#Tuples -> they are immutable (we cannot append , remove or change elements)

x = (0,0,2,2)

#unpacking tuple

t=(1,2,3)
a,b,c =t #now a=1 , b=2 , c=3

q = (1,2,3,4,5,6,7)

A,B,*C = q #A=1 , B=2 , C=[3,4,5,6,7]


#Sets: unordered collection of elements

#no dublicate elements , its just used for lookups (to see if something is there or not) ,removal and addition

x = set() #use to create empty set

s = {4,3,5,6} #set literal (use when you are not creating empty set)

s= {} # this becomes dictionary

s.dd(5)
s.remove(3)

print(4 in s) #gives true or false based on the element is in the set or not

#we can do operations on sets like:
# s1.union(s2) , s1.intersection(s2)
# s1.difference(s2)


#Dicts :its a key value pair like hashmap 

x = {'key': 4}

print(x['key'])

#to add new key and every key may not be of same data type

x['key2'] = 5
x[2] = 100 #this is also a key

print(list(x.values())) 
print(list(x.keys())) 

del x['key'] #to del a key


