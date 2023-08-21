class Solution:
    def maxProfit(self, prices):
        l,r,p = 0,1,0
        while r<len(prices):
            c = prices[r] - prices[l]
            if prices[l] < prices[r]:
                p = max(c,p)
            else:
                l=r
            r+=1
        return p