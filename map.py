def add (x,y):
    return(x+y)
a=[1,2,3,4,5,6,7,8,9]
b=[3,4,2,5,1,4,2,6,4]
result=map(add,a,b)
print(list(result))

def sq (t):
    return(t*t)
w=[1,5,4,6,3,5,3]
result=map(sq,w)
print(list(result))
    

       