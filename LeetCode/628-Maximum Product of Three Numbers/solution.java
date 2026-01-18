import java.util.Arrays;

class Solution {
    public int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        
        int n = nums.length;
        int a = nums[n - 1];
        int b = nums[n - 2];
        int c = nums[n - 3];
        
        int x = nums[0];
        int y = nums[1];
        
        int product1 = a * b * c;
        int product2 = x * y * a;
        
        return Math.max(product1, product2);
    }
}

// 628. Maximum Product of Three Numbers

// Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

// Example 1:

// Input: nums = [1,2,3]
// Output: 6
// Example 2:

// Input: nums = [1,2,3,4]
// Output: 24
// Example 3:

// Input: nums = [-1,-2,-3]
// Output: -6
 

// Constraints:

// 3 <= nums.length <= 104
// -1000 <= nums[i] <= 1000
 
