# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
class Solution:
    def maxSubArray(self, nums: list) -> int:
        n_sum = nums[0]
        max_s = n_sum
        for n_i in nums[1:]:
            if n_sum + n_i < n_i:
                n_sum = n_i
            else:
                n_sum += n_i
            max_s = max(max_s, n_sum)
        return max_s