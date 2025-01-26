list1 = [1,2,3,4,5,6]
result =[]
sum = 0
for i in range(len(list1),0,-1):
    result.append(i)
    sum = sum +i
print(result)
print(sum)
print(sum/len(list1))