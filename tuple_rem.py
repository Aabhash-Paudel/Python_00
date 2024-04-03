a = tuple(map(int, input().split()))
b = int(input()) #3
a=a[:b]+a[b+1:]
print(a)


