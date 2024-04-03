a=list(map(int,input().split()))
list2=[]
a.sort() # [2,3,4,5,6,7]
for i in a:
    if(i%2==0):
        list2.insert(0,i)
    else:
        list2.append(i)
print(list2)