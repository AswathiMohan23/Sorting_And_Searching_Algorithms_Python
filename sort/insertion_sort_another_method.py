def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i # innerloop starts at the index of outer loop and iterates the list to left and check
                # whether we need to swap
        while arr[j - 1] > arr[j] and j > 0: # if next neighbour is bigger than the current element
                # and we need to swap. we dont want j=0 because if j=0 then when we check arr[j-1], it will become 0-1 =-1
                # and -1 index wont be there
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1 # we need to go to left after the swap


if __name__ == "__main__":
    arr = [2, 6, 5, 1, 3, 4]
    insertion_sort(arr)
    print(arr)
