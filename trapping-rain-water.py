# https://leetcode.com/problems/trapping-rain-water/

def trap(height: list[int]) -> int:
    water = 0

    l = len(height)

    dp_l = [0] * l
    dp_l[0] = height[0]
    for i in range(1, l):
        dp_l[i] = max(dp_l[i-1], height[i])

    dp_r = [0] * l
    dp_r[-1] = height[-1]
    for i in range(l - 2, -1, -1):
        dp_r[i] = max(dp_r[i+1], height[i])

    for i in range(1, len(height) - 1):
        water += max(0, min(dp_l[i], dp_r[i]) - height[i])
    return water
