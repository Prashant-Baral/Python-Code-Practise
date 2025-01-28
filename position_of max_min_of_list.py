li = list(map(int, input("Enter the memebers of the list").split()))
max1= li[0]
min1= li[0]
for i in li:
    if i>max1:
        max1=i
    if i<min1:
        min1=i
print(max1)
print(min1)


