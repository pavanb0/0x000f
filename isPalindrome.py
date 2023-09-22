class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if reversed(str(x)) == str(x) else False
