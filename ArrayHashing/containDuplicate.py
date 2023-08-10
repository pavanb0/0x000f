class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return False if (len(nums)==len(set(nums))) else True
        
sol = Solution()
print(True) if sol.containsDuplicate([1111,111,0000]) else print(False)