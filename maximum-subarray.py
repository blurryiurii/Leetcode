# https://leetcode.com/problems/maximum-subarray/
def maxSubArray(nums: list[int]) -> int:
    
    if len(nums) == 1:
        return nums[0]
    
    maxSum = max()
    prefix = 0
    for i in range(len(nums)):
        prefix += nums[i]
        maxSum = max(prefix, maxSum)
        if prefix < 0:
            prefix = 0
    return maxSum