# 977. Squares of a Sorted Array
# Solution without good complexity O(nlogn) because of the sort function. 
# I will try to add another solution with a complexity of O(n) using two pointers, in the comming days.
# 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq = []
        for i in nums: 
            sq.append(i** 2)
        
        sq.sort()
        return sq


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
 
