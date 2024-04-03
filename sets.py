s = set()
print(s)

s=set((1,2,'hi','hello'))
print(s)
print(type(s))


s= {1,2,4,'ok','whats up'}
print(s)

for i in s:
    print(i)
#del s can delete the set
print(s)

s =set((1,2,3))
print(type(s))

#set methods
x= {1,3,4,5}
x.add("hello") #using add to add an element is set
print(x)

#using pop
z = x.pop()
print(z)
#using update

y = {'hi','whatsup'}
y.discard("hi") # removed hi from y set and if its empty--> no error
x.update(y)
print(x)


print(x.intersection_update(y))
a={1,2,4,5}
b={1,4,5}
print(a.intersection_update(b))

a.symmetric_difference_update(b)
print(a)
a={5,2,0,10}
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sorted(a))
print(any(a))
print(all(a))
b = frozenset([1,3,4,5])
print(b)