class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        nums = set(nums) 
        longest_streak = 0
        
        for num in nums:
            if num - 1 not in nums:
                current_num = num
                current_streak = 1
                while current_num + 1 in nums:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak        
