# 977. Squares of a Sorted Array
# Solution without good complexity O(nlogn) because of the sort function. 
# This is solution with a complexity of O(n) using two pointers.
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # sq = []
        # for i in nums: 
        #     sq.append(i** 2)
        
        # sq.sort()
        # return sq

        n = len(nums)   # taille 
        left = 0        #first pointer
        right = n-1     #sec pointer
        pos = n-1
        res = [0]*n     # array withindex

        while left <= right : 
            left_sq = nums[left]**2    # ^2
            right_sq = nums[right]**2  # ^2

            if left_sq > right_sq: 
                res[pos] = left_sq
                left += 1 
            else : 
                res[pos] = right_sq
                right -= 1 

            pos -= 1 
        return res


#977. Squares of a Sorted Array

#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

#Example 1:

#Input: nums = [-4,-1,0,3,10]
#Output: [0,1,9,16,100]
#Explanation: After squaring, the array becomes [16,1,0,9,100].
#After sorting, it becomes [0,1,9,16,100].
#Example 2:

#Input: nums = [-7,-3,2,3,11]
#Output: [4,9,9,49,121] 

#Constraints:

#1 <= nums.length <= 104
#-104 <= nums[i] <= 104
#nums is sorted in non-decreasing order.
 
