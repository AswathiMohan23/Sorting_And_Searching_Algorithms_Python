# Given a sorted array of distinct integers and a target value, return the index if the
# target is found.If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1, 3, 5, 6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1, 3, 5, 6], target = 7
# Output: 4

def solution(num_list, target):
    for index,element in enumerate(num_list):
        if element==target:
            return index
        else:

            for i in range(len(num_list)):
                for j in range(0,len(num_list)-i-1):
                    if num_list[j]<target and num_list[j+1] > target:
                        return j+1




if __name__ =="__main__":
    print(solution([1, 3, 5, 6], 5)) # 2
    print(solution([1, 3, 5, 6], 2)) #1
