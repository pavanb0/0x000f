class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res=[]
        count=0
        for i in range(len(s)):
            if len(res)==0:
                count+=1
                res.append(s[i])
            elif res[len(res)-1]!=s[i]:
                res.remove(res[len(res)-1])
            else:
                res.append(s[i])
        return count
