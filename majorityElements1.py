class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        nums = sorted(nums)
        return nums[len(nums)//2]
   
