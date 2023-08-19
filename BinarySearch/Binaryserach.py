class Solution:
    def search(self, nums, target) :
        for i,j in enumerate(nums):
            if j == target:
                return i
        return -1