class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        popen, result = 0, []
        for x in s:
            if x==')':
                popen -= 1
            if popen>0:
                result.append(x)
            if x=='(':
                popen += 1
        return ''.join(result)  
