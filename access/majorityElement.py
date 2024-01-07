class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        i,k = 0 ,0
        for p in nums:
            if i == 0:
                k = p
            elif p == k:
                i+=1
            else:
                i-=1
        return k
        
