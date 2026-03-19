# 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr_low = 0
        ptr_i = 0 
        ptr_high = len(nums) -1

        while ptr_i <= ptr_high: 
            if nums[ptr_i] == 0 : 
                nums[ptr_i], nums[ptr_low] = nums[ptr_low], nums[ptr_i]
                ptr_low += 1
                ptr_i += 1
            elif nums[ptr_i] == 2 : 
                nums[ptr_i], nums[ptr_high] = nums[ptr_high], nums[ptr_i]
                ptr_high -= 1
            else:
                ptr_i += 1  


# 75. Sort Colors

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

 
# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 
