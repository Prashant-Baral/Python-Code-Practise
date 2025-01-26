def mergesort(arr):
    if len(arr)<=1 :
        return arr
    
    mid= len(arr)//2;
    left_half=arr[:mid]
    right_half =arr[mid:]

    left_sorted= mergesort(left_half)
    right_sorted = mergesort(right_half)

    return mergelist(left_sorted,right_sorted)




def mergelist(list1,list2):
    i,j=0,0
    mrg_lst=[]

    while(i<len(list1) and j<len(list2)):
        if(list1[i]<list2[j]):
            mrg_lst.append(list1[i])
            i+=1
        else:
            mrg_lst.append(list2[j])
            j+=1

    while(i<len(list1)):
        mrg_lst.append(list1[i])
        i+=1

    while(j<len(list2)):
        mrg_lst.append(list2[j])
        j+=1
    return mrg_lst


def get_input_data(prompt):
    user_input =input(prompt)
    return list(map(int,user_input.split()))

list1= get_input_data("Enter first list: ")


mrged_list=mergesort(list1)
print(mrged_list)