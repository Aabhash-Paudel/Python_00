a = tuple(map(int, input("Enter the numbers with spaces: ").split()))
for i in a:
    count = 0
    for j in a:
        if i == j:
            count += 1
print(count)