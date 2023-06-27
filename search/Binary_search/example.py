# time complexity is O(log2 n) ie, log to the base n means how many times a num should be divided by 2 to get 1

def binary_search(num_list, key):
    start = 0
    end = len(num_list) - 1
    while start<=end:
        mid =(start+end)//2
        if num_list[mid]==key:
            return mid+1
        elif num_list[mid]<key:
            start=mid+1
        elif num_list[mid]>key:
            end=mid-1
    return -1  #if middle element is not found

if __name__=="__main__":
    position=binary_search([1,2,34,56,78,90],78)
    if position!=-1:
        print("element found at ",position)
    else:
        print("element not found")
