def func() :
    print('run')

func()    

def multi(x,y):
    return x*y , x/y #we get the ans in form of tuple

r1,r2 = multi(5,6) #this will seperate the answers

print(r1,r2)

#lambda :one line anon fnc

x = lambda x : x+5

print(x(2)) # 7

# map and filters

x = [1,2,3,4,5,6,7,8,9,0]

mp = map(lambda i: i+2 , x)

print(list(mp)) #all elements will be added by 2 and a new list will be given


x = [1,2,3,4,5,6,6,7,8,9,0,10,22,24,50]

fil = filter(lambda i: i%2 ==0 , x) #it will filter out the values from list which are even
print(list(fil))
