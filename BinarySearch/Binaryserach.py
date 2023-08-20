class Solution:
    def search(self, nums, target) :
        for i,j in enumerate(nums):
            if j == target:
                return i
        return -1
    
    # it's not binary search but runtime beats 92% and memory around 80%