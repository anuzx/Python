a =0
b =1

n= int(input("enter the no.of terms you want: "))

print(a,b,end=" ")
while(n-2):
    c=a+b
    a=b
    b=c
    print(c , end=" ")
    n=n-1
       


#using recursion

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter n: "))
print(f"The {n}th Fibonacci term is:", fibonacci(n))
