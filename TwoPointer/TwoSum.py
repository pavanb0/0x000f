class Solution:
    def twoSum(self, numbers, target) :
        l , r = 0 , len(numbers)-1
        while l < r:
            su = numbers[l] + numbers[r]
            if su < target:
                l+=1
            elif su > target:
                r-=1
            else:
                return [l+1,r+1]