class Solution:
    def searchMatrix(self, matrix, target) :
        mat = []
        for i in matrix:
            for j in i:
                mat.append(j)
        left,right = 0,len(mat)-1
        while left<=right:
            mid = (left+right) // 2
            if mat[mid] == target:
                return True
            elif mat[mid]<target:
                left = mid + 1
            else:
                right = mid - 1
        return False