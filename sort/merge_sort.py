def merge_sort(list1):
    if len(list1)>1:
        mid = len(list1)//2
        left_list=list1[:mid] # if we didnt mention anything before ':' means it starts from 0.
        right_list=list1[mid:] # if we didnt mention anything after ':' means it takes all the elements till end
        merge_sort(left_list)
        merge_sort(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list): # here i and j are index and index will be always less than the length
                # of the list
            if left_list[i]<right_list[j]:
                list1[k]=left_list[i]
                i=i+1
                k=k+1
            else:
                list1[k]=right_list[j]
                j=j+1
                k=k+1
        while i<len(left_list):
            list1[k]=left_list[i]
            i = i + 1
            k = k + 1

        while j < len(right_list):
            list1[k] = right_list[j]
            j = j + 1
            k = k + 1



if __name__=="__main__":
    list1=[2,3,5,1,7,10,8,6,4]
    merge_sort(list1)
    print(list1)