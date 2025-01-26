list1= list(map(int,input("ENter the members of the list: ").split()))
list2= list(map(int,input("Enter the elements of the second list: ").split()))
list3=[]
if(len(list1)!=len(list2)):
    print("The length of the list should be the same.")
else:
    list3=[max(i,j) for i,j in zip(list1,list2)]
print(list3)

print(f"The greatest element of the list1 is{max(list1)}")
print(f"The greatest element of the list2 is {max(list2)}")
print(f"The greatest element of the list3 is{max(list3)}")

