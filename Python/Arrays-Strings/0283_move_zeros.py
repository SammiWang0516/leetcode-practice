# 283. Move Zeros
'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
'''
def moveZeros(nums):
    read_pointer = 0
    write_pointer = 0
    n = len(nums)
    while write_pointer < n:
        if read_pointer == n:
            nums[write_pointer] = 0
            write_pointer += 1
        else:
            if nums[read_pointer] != 0:
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1
                read_pointer += 1
            else:
                read_pointer += 1
    return nums
'''
def moveZeros(nums):
    n = len(nums)
    count = 0
    for value in nums:
        if value == 0:
            count += 1
    move_time = 0
    index = 0
    while move_time < count:
        if nums[index] == 0:
            nums.append(0)
            nums.pop(index)
            move_time += 1
        else:
            index += 1
    return nums
'''
nums = [0,1,0,3,12]
print(moveZeros(nums))