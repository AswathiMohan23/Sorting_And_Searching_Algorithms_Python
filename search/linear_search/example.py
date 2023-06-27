# efficiency of linear search will be proportional to the size of the data
# time complexity is O(n)

def linear_search(l,key): # key is the element to be searched
    for index,element in enumerate(l): # enumerate gives the element and the position of that element in that list
        if key == element:
            print("item found at ",index)
            break
    else:
        print("item not found")

if __name__=="__main__":
    linear_search([34,22,56,77,93,45],77)
    linear_search([34,22,56,77,93,45],1)
