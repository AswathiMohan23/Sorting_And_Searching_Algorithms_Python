# selection sort in ascending order
list1=[56,3,2,78,6,0]
for i in range(len(list1)):
    min_val=min(list1[i:]) #find out min value and place at oth index
    min_index=list1.index(min_val,i) # finding index of min value... here i is given for the code to work
                    # for duplicate values
    list1[i],list1[min_index]=list1[min_index],list1[i] # swapping the index

print(list1)
