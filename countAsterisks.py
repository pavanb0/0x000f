class Solution:
    def countAsterisks(self, s: str) -> int:
        c=0
        flag=False
        for i in s:
            if (i=='|'):
                flag=not(flag)
            if(i=='*' and flag==False):
                c=c+1
        return c
