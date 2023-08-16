class Solution:
    def twoSum(self, nums, target):
        dictionary={}
        for i in range(len(nums)):
            x= target-nums[i]
            if(x in dictionary):
                return [dictionary[x],i]
                break
            else:
                dictionary[nums[i]]=i
        return []
