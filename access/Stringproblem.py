class Solution:
    def defangIPaddr(self, address: str) -> str:
        out = ""
        for i in address:
            
            if i == ".":
                out+="[.]"
            else:
                out+=i
        return out
