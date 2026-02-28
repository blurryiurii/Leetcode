# https://leetcode.com/problems/find-in-mountain-array/

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        """binary search with extra steps"""

        l = mountainArr.length() - 1

        # find peak, where slope switches
        left, right = 0, l
        while left <= right:
            mid = (left + right) // 2

            one = mountainArr.get(mid)
            two = mountainArr.get(mid+1)

            if one < two: # positive slope, set left bound
                left = mid + 1
            else:   # negative slope, must be left of here
                right = mid - 1

        print("mid", mid)

        left, right = 0,  mid
        # search left of peak first, to return minimum index.
        while left <= right:
            m = (left + right) // 2
            print("checking", m)
            cur = mountainArr.get(m)

            if cur < target:
                left = m + 1
            elif cur > target:
                right = m - 1
            else:
                return m

        # search right side
        left, right = mid, l
        while left <= right:
            m = (left + right) // 2
            cur = mountainArr.get(m)

            if cur > target:
                left = m + 1
            elif cur < target:
                right = m - 1
            else:
                return m
        return  -1

