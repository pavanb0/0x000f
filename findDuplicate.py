class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ar = {}
        for i in nums:
            if i in ar:
                return i

            else:
                ar[i] = 1
