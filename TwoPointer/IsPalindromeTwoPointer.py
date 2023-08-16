class Solution:
    def isPalindrome(self, s: str) -> bool:
        lef,rig =0,len(s)-1
        while lef<rig:
            while lef < rig and not self.isPal(s[lef]):
                lef += 1
            while rig > lef and not self.isPal(s[rig]):
                rig -= 1
                
            if s[lef].lower() != s[rig].lower():
                return False
            lef+=1
            rig-=1

        return True

    def isPal(self,s):
        return (ord('A')<=ord(s)<=ord('Z') or
        ord('a') <= ord(s) <= ord('z') or 
        ord('0') <= ord(s) <= ord('9'))