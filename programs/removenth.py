s = input("enter the string: ")
n = int(input("enter the number: "))

def removenth(s,n):
  
    
    if n>=len(s):
        print(s) 
    elif n<0 :
        print("wrong input")
    else :
        #removal is done using slicing
      str = s[0:n] + s[n+1:]
      print(str)
       
       
            
removenth(s,n)     