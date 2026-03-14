# 283. Move Zeroes
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zeroes.
# Solutiion with O(n) time complexity and O(1) space complexity.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0

        for j in range(len(nums)): 
            if nums[j] != 0 :
              nums[i] = nums[j]
              i += 1
            else : 
              nums[j] == 0
            
        for k in range(i, len(nums)):
           nums[k] = 0



# 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 