a = input("Enter a number: ")

list1 = [int(i) for i in a]  # Convert the input to a list of integers
list1.sort()
print(sum(list1[:3]))

# #alternative 

# a=list(map(int,input().split()))
# a.sort()
# print(sum(a[:3]))