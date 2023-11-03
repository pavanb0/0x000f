class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target>max(nums): 
            return len(nums)
        else:
            for i in range(len(nums)):
                if nums[i] >= target:
                    return i
        
