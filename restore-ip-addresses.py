# https://leetcode.com/problems/restore-ip-addresses/

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        spl = s.split(".")
        if len(spl) == 1:
            d = []
            tmp = self.restoreIpAddresses(s[0]+"."+s[1:])
            if tmp:
                d.append(tmp)
            tmp = self.restoreIpAddresses(s[0:2]+"."+s[2:])
            if tmp:
                d.append(tmp)
            tmp = self.restoreIpAddresses(s[0:3]+"."+s[3:])
            if tmp:
                d.append(tmp)
        elif len(spl) == 2:
            pre, post = spl
            d = []
            tmp = self.restoreIpAddresses(pre+"."+s[0]+"."+s[1:])
            if tmp:
                d.append(tmp)
            tmp = self.restoreIpAddresses(pre+"."+s[0:2]+"."+s[2:])
            if tmp:
                d.append(tmp)
            tmp = self.restoreIpAddresses(pre+"."+s[0:3]+"."+s[3:])
            if tmp:
                d.append(tmp)
        elif len(spl) == 3:
            pre, post = spl[0:2], spl[2]
            d = []
            tmp = self.restoreIpAddresses(pre+"."+s[0]+"."+s[1:])
            if tmp:
                d.append(tmp)
            tmp = self.restoreIpAddresses(pre+"."+s[0:2]+"."+s[2:])
            if tmp:
                d.append(tmp)
            tmp = self.restoreIpAddresses(pre+"."+s[0:3]+"."+s[3:])
            if tmp:
                d.append(tmp)
        elif len(spl) == 4:
            a, b, c, d = spl
            if int(a) in range(0, 256) and int(b) in range(0, 256) and \
               int(c) in range(0, 256) and int(d) in range(0, 256):
                return s
            return ""
        return tmp
