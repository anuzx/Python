# == checks for equality 
# other: != , <= , >= , < , >

print(ord("a")) #this will tell the ASCII value

#if else 

x = int(input("Enter the number: "))

if x%2 == 0 :
    print(x ,"is an even number")
else:
    print(x , "is a odd number")



#while and for loop



for i in range(10): #start , stop , step (by default if you dont put anything it will take stop value)
    print(i)

x = [3,4,5,6]

for i,element in enumerate(x):#create index and values for all the elements
    print(i , element)

#for item in sequence

fruits =["apple" , "banana" , "pineapple"]
for fruit in fruits:
    print(fruit)


#while loop

i=0
while i<10:
    print("run")
    i += 1
    i *= 2