class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        v = sorted(strs)
        f = v[0]
        l = v[-1]
        for k in range(min(len(f),len(l))):
            if(f[k]!=l[k]):
                return ans
            ans += f[k]
        return ans
