# https://leetcode.com/problems/palindromic-substrings/
# O(n^2). brute force approach is O(n^3)

def countSubstrings(s: str) -> int:
    summ = 0
    ln = len(s)

    for i in range(0, ln):
        # 2ptr approach, iterating outwards
        
        # ODD length
        l = h = i
        while l >= 0 and h < ln and s[l] == s[h]:
            summ += 1
            l -= 1
            h +=1

        # EVEN length
        l, h = i, i+1
        while l >= 0 and h < ln and s[l] == s[h]:
            summ +=1
            l -= 1
            h += 1

    return summ

# to avoid repetitiveness, we can also construct a function
# that takes in a string, l, and h values to return the number
# of palindromes
# this function would be called once for odd-lengths, and once for
# even lengths. 