# most frequent  element in the list:

"""list1 = list(map(int,input("Enter the elements of the list: ").split()))
counts = {}

for item in list1:
    counts[item] = counts.get(item,0)+1
print(counts)
max_frequency = max(counts.values())
max_frequent= [key for key, value in counts.items() if value==max_frequency]
print(max_frequent)"""


#To check if the no of occurences of elements is unique in array/list is unique or not:
"""from typing import List

class Solution:
    def uniqueoccur(self,arr: List[int])->bool:
        counts={}
        for item in arr:
            counts[item] = counts.get(item,0)+1

        values= list(counts.values())
        return len(values)==len(set(values))


if __name__ == "__main__":
    arr = [1,1,2,2,3,1,2]
    soln = Solution()
    print(soln.uniqueoccur(arr))"""

# To calculate the length of the list

"""list1= [1,1,2,2,3,1,3,4]
length = 0
for item in list1:
    length=length+1
print(length)"""

    
# to reverse a list:
"""list1 = [1,2,3,4,5,6]
result =[]
sum = 0
for i in range(len(list1),0,-1):
    result.append(i)
    sum = sum +i
print(result)
print(sum)
print(sum/len(list1))"""

#to find second largest number in the list

list1 =[1,2,3,4,5,6,7,8]
max1= max(list1)
smin=list1[0]
for i in list1:
    if (i < max1):
        smin=i
print(smin)
    
    



