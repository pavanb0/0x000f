class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ar = set()
        out = 0
        l = 0
        m = 0
        while l < len(s):
            if s[l] not in ar:
                ar.add(s[l])
                l+=1
                out = max(len(ar),out)
            else:
                ar.remove(s[m])
                m+=1
        return out


