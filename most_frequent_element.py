list1 = list(map(int,input("Enter the elements of the list: ").split()))
counts = {}

for item in list1:
    counts[item] = counts.get(item,0)+1
print(counts)
max_frequency = max(counts.values())
max_frequent= [key for key, value in counts.items() if value==max_frequency]
print(max_frequent)

