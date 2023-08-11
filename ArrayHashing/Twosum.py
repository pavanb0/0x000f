class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary={}
        for i in range(len(nums)):
            x= target-nums[i]
            if(x in dictionary):
                return [dictionary[x],i]
                break
            else:
                dictionary[nums[i]]=i
        return []
