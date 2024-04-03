
a =tuple(map(int, input("Enter the numbers with spaces: ").split()))

b= int(input("Enter the search key: "))
if b in a:
    b= a.index(b)
    print(b)
else:
    print("the element is not present in the tuple")
