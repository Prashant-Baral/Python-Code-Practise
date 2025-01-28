li = list(map(int,input("Enter the elements of the list").split()))
counts = {}
for item in li:
    if item in counts:
        counts[item]+=1
    else:
        counts[item]=1

for key,value in counts.items():
    if value>1:
        print(key)

