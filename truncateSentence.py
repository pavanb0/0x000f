class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        return ' '.join(map(str,s[0:k]))
        

        
