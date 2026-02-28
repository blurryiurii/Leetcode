
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = list()
        for s in strs:
            srtd = sort(s)

            # try to match to a group
            for i in range(len(groups)):
                if srtd == sort(groups[i][0]):
                    groups[i].append(srtd)
                    break
            else:
                groups.append([s])