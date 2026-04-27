list1=[2,4,6,8,10,12,14,16,18,20]
list2=[1,3,5,7,9,11,13,15,17,19]

result=zip(list1,list2)
print(list(result))

list3=(10,20,30,40,50)
list4=(100,200,300,400,500)
for x,y in zip(list3,list4[::-1]):
    print(x,y)
