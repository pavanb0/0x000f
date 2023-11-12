class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        di = {}

        n= len(nums)//2

        for i in nums:
            if i not in di:
                di[i] = 1
            else:
                value = di.get(i,None)
                di[i] = value+1
        for i,j in di.items():
            if j == n:
                return i
            
            
        
