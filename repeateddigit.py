a = input("Enter number with space: ").split() 
c = []

for i in a:
    if a.count(i)%2!=0 and i not in c:
        c.append(i)
print(c)