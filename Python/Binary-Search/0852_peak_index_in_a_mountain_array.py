# 852 Peak Index In A Mountain Array
'''
You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.
Return the index of the peak element.
Your task is to solve it in O(log(n)) time complexity.

Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Example 3:
Input: arr = [0,10,5,2]
Output: 1
'''
def peakIndexInMountainArray(arr):
    # classic binary search question
    # instead of finding the exact target value
    # use the middle value to compare with left side and right side value
    # if the value we chose is larger than both sides of value, it is the answer
    def binary_search(arr, start, end):
        # find the middle index first
        middle = (start + end) // 2
        # if the subarray touch the first element
        if middle == start:
            # if the first element is the peak
            if arr[middle] > arr[middle+1]:
                return middle
            # has to be the next element
            else:
                return middle+1
        # if the subarray touch the last element
        elif middle == end:
            # if the last element is the peak
            if arr[middle] > arr[middle-1]:
                return middle
            # has to the next element
            else:
                return middle-1
        else:
            if arr[middle] > arr[middle-1] and arr[middle] > arr[middle+1]:
                return middle
            elif arr[middle] < arr[middle-1]:
                return binary_search(arr, start, middle-1)
            elif arr[middle] < arr[middle+1]:
                return binary_search(arr, middle+1, end)
    return binary_search(arr, 0, len(arr)-1)
arr = [3,9,8,6,4]
print(peakIndexInMountainArray(arr))
# output = 1 (index but not value itself)