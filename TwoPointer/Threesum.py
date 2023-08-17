def threesum(nums):
    out = []
    if len(nums)<=0:
        return []
    nums = nums.sort()

    for i in range(len(nums)-2):
        j,k = i+1,len(nums)-1
        # start = nums[i]
        while j<k:
            sums = nums[i] + nums[j] + nums[k]
            print(sums)
            

        
nums = [-1,0,1,2,-1,-4]
print(sorted(nums))
# threesum(nums)
# [-1,0,1] and [-1,-1,2].