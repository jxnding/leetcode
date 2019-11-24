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


#### Booty solution I came up with during a test...
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def newMax(i,j,k):
#             nonlocal longest, start, end
#             if k-j-2+1>longest[i]:
#                 longest[i] = k-j-2+1 #overcounted by 2
#                 start[i] = j+1
#                 end[i] = k-1
#         if s=="":
#             return ""
#         longest = [1]*len(s) #min length = 1
#         start = [0]*len(s)
#         end = [0]*len(s)
#         for i in range(len(s)):
#             # Odd length palindrome
#             j = k = i
#             while j>=0 and k<len(s) and s[j]==s[k]:
#                 j-=1
#                 k+=1
#             newMax(i,j,k)
#             # Even length palindrome
#             j, k = i, i+1
#             while j>=0 and k<len(s) and s[j]==s[k]:
#                 j-=1
#                 k+=1
#             newMax(i,j,k)
#         return s[start[longest.index(max(longest))] : end[longest.index(max(longest))]+1]