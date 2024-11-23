# https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs: list[str]) -> str:
    tot = 0
    min_len = len(min(strs, key=len))  # grab length of longest string
    list_len = len(strs)
    if not min_len:
        return ""
    if list_len == 1:
        return strs[0]
    # check the ith char of each string
    for i in range(1, min_len + 1):
        cur_char = strs[0][tot]
        for i in range(list_len):
            if strs[i][tot] != cur_char:
                return strs[0][:tot]
        tot += 1
    return strs[0][:tot]