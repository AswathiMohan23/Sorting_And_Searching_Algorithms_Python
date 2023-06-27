# Insertion Sort : This sorting algorithm maintains a sub-array that is always sorted.
# Values from the unsorted part of the array are placed at the correct position in the sorted part.
# It is more efficient in practice than other algorithms such as selection sort or bubble sort.
# Insertion Sort has a Time-Complexity of O(n2) in the average and worst case, and O(n) in the best case.

# Explanation
# step1 : here we consider first element as sorted element and rest as unsorted.
# step 2 :Take the first element in the unsorted part as un1 and compare it with sortedpart element s1.
# step 3: if un1< s1 then insert u1 in the correct index. Else leave it as it is.
# step 4 : take next element in unsorted part and compare it with sorted elements
# step 5 : repeat 3 and 4 until all elements are sorted

def insertion_sort(list1):
    # Outer loop to traverse on len(list1)
    for i in range(1, len(list1)):

        current_element = list1[i]

        position = i - 1  # get zero th position

        while position >= 0 and current_element < list1[position]: # position >0 is given because we need stopping condition
            # and in first stage it should execute 1 time, in second stage it should execute 3 times and so on

            list1[position + 1] = list1[position]
            position = position - 1

        list1[position + 1] = current_element

    return list1


if __name__ == "__main__":
    list1 = [7, 2, 1, 6]
    print("The unsorted list is:", list1)
    print("The sorted new list is:", insertion_sort(list1))
