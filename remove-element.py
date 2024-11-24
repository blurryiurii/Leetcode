# https://leetcode.com/problems/remove-element/

def removeElement(self, nums: list[int], val: int) -> int:
    # remove elements
    k = len(nums)
    for i in range(k - 1, -1, -1):
        if nums[i] == val:
            nums.pop(i)
            k -= 1
    return k