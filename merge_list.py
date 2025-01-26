def mergelist(list1,list2):
    i,j=0,0
    mrg_list=[]

    while i<len(list1) and j<len(list2):
        if(list1[i]<list2[j]):
            mrg_list.append(list1[i])
            i+=1
        else:
            mrg_list.append(list2[j])
            j+=1


    while(i<len(list1)):
        mrg_list.append(list1[i])
        i+=1
    
    while(j<len(list2)):
        mrg_list.append(list2[j])
        j+=1
    return mrg_list

def get_input_list(prompt):
    a= input(prompt)
    return list(map(int,a.split()))

list1= get_input_list("Enter the first list")
list2= get_input_list("Enter the second list")
merged=mergelist(list1,list2)
print("Merged List:",merged)