class Solution:
    def dailyTemperatures(self, temperatures):
        if len(temperatures) <= 0:
            return []
        start,end,out = 0,len(temperatures)-1,[]
        while start<=end:
            cur = temperatures[start]
            nd = start
            ctr = 0
	            while nd < end:
                 if temperatures[start] < temperatures[nd+1]:
                    ctr+=1
                    break
                nd+=1
            out.append(ctr)
            start+=1
        return out
temperatures = [73,74,75,71,69,72,76,73]
Solutions = Solution()
print(Solutions.dailyTemperatures(temperatures))
