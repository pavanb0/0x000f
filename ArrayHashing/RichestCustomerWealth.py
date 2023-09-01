class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        out = 0
        for i in accounts:
            su = 0
            for s in i:
                su+=s
                out = max(su,out)
        return out

        
