# selection sort in descending order

if __name__=="__main__":
    list1=[56,3,2,78,6,0]
    for i in range(len(list1)):
        max_val=max(list1[i:]) #find out max value and place at zero th index
        max_index=list1.index(max_val)# # finding index of max value... here i is given for the code to work
                    # for duplicate values
        list1[i],list1[max_index]=list1[max_index],list1[i] # swapping the index

    print(list1)
