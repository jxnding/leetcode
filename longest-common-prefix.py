class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)<1: return ''
        ans = -1
        for i, n in enumerate(strs[0]):
            good = True
            for s in strs:
                if i>=len(s): good = False
                elif s[i]!=n: good = False
            if good:
                ans = i
            else: 
                break
        return strs[0][:ans+1]
#### O(m*n), O(1)
# 2/29

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs==None:
            return ""
        if strs==[]:
            return ""
        if len(strs)==1:
            return strs[0]
        prefix = ""
        currChar = ""
        
        i = 0
        while True:
            if i>=len(strs[0]):
                return prefix
            currChar = strs[0][i]
            for j in range(1, len(strs)):
                if i>=len(strs[j]):
                    return prefix
                if strs[j][i]!=currChar:
                    return prefix
            prefix+=currChar
            i+=1

#We're optimal, O(n) with O(1) space
#Nifty solution:
# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs: return ""
#         if len(strs) == 1: return strs[0]
        
#         strs.sort()
#         p = ""
#         for x, y in zip(strs[0], strs[-1]):
#             if x == y: p+=x
#             else: break
#         return r