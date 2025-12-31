#data types -> int , float , string , bool

#input

name = input("Name: ")
print ("hello",name)

#exponent -> x**y (x to the power y)

# // -> this gives integer result of the division

# % -> gives remainder
 
num = input("Number: ")
print(int(num)-5) #by default num will be a string 

#string methods

#.upper() -> converts the string into upper case

#.lower() ->lowercase

#.capitalize() -> makes the first char of string capital

x ='hello'
y = 3
print(x*y) #hellohellohello

x ='hello'
y = 'yes'
print(x+y) #helloyes

#slice operator

x = [0,1,2,3,4,5,6,7,8,9]
y = ['hi' , 'hello' , 'bye']
s="hello"
sliced = x[0:4:2] #start:stop:step (we put the value of index) , index at stop we will not be included 

#last index in python is taken as -1

#to reverse the list we can do x[::-1] , slice operator works on string , tuples too 




