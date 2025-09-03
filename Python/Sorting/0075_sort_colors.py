# 75 Sort Colors
'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
'''
def sortColors(nums):

    # if i need to sort the array in-place
    # quick sort shall be used
    # use of 3-way partitioning (refined quicksort)
    def quicksort(array, start, end):
        # base case of quicksort: start is greater or equal to end
        # return stops the recursion
        if start >= end:
            return
        start_pivot, end_pivot = partition(array, start, end)
        quicksort(array, start, start_pivot-1)
        quicksort(array, end_pivot+1, end)

    def partition(array, start, end):
        # use of 3-way quicksort requires 3 variables
        i = start                       # interator for the whole array
        left = start                    # check the left bound of same value of pivot
        right = end                     # check the right bound of same value of pivot
        pivot_value = array[start]      # pick the first element as the pivot value
        while i <= right:
            if array[i] == pivot_value:
                i += 1
            elif array[i] < pivot_value:
                array[i], array[left] = array[left], array[i]
                left += 1
                i += 1
            else:
                array[i], array[right] = array[right], array[i]
                right -= 1
        return left, right
    quicksort(nums, 0, len(nums)-1)
    return nums

nums = [2, 0, 1, 3, 4, 5]
print(sortColors(nums))