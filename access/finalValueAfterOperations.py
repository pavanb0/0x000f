class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        out = 0 
        for i in operations:
            if i == "++X" or i == "X++":
                out+=1
            else:
                out-=1
        return out
