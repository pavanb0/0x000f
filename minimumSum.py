class Solution:
    def minimumSum(self, num: int) -> int:
        arr = list(str(num))
        arr.sort()
        return int(arr[0]+arr[2]) + int(arr[1]+arr[3])
