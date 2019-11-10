import pdb
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(c):
            i, j = c,c
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]
        ans = ""
        for c in range(len(s)):
            curr = expand(c,c)
            if len(curr)>len(ans):
                ans = curr
            curr = expand(c,c+1)
            if len(curr)>len(ans):
                ans = curr
        return ans
print(Solution().longestPalindrome("baba"))