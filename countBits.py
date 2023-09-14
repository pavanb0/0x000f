class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        i=1
        while i<=n:
            i2=min(i<<1, n)
            for j in range(i, i2+1):
                ans[j]=ans[j-i]+1
            i<<=1
        return ans
