nums = []
target= 0
left,right = 0,len(nums)-1
while left<=right:
    mid = (right+left) // 2
    if nums[mid] == target:
        print(mid)
    elif nums[mid]<target:
        left = mid +1
    else:
        right = mid -1