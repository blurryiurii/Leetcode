# https://leetcode.com/problems/3sum/

def threeSum(nums: list[int]) -> list[list[int]]:
    triples = list()
    lnums = len(nums)

    nums.sort()

    for i, num in enumerate(nums):
        # if we are checking the same num
        if i > 0 and nums[i - 1] == num:
            continue

        l = i + 1
        r = lnums

        while l < r:
            threeSum = num + nums[l] + nums[r]
            if threeSum < 0:
                l += 1
            elif threeSum > 0:
                r -= 1
            else:
                triples.append((num, nums[l], nums[r]))
                l += 1
                while nums[l] == nums[l - 1]:
                    l += 1

    return triples
