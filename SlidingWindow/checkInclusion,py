class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not len(s1) <= len(s2):
            return False
        l, s1len = 0, len(s1)
        while l + s1len <= len(s2):  
            st = ""
            for i in range(l, l + s1len):  
                st += s2[i]
            if sorted(s1) == sorted(st):
                return True
            l += 1
        return False
