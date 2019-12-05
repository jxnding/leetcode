import pdb
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)<=1:
            return 0
        # Trim beginning
        i=0
        while s[i]==')':
            i+=1
        s=s[i:]
        
        opens = []
        maxLength = 0
        latest = -1
        for i, c in enumerate(s):
            if c=='(':
                opens.append(i)
            else:
                if opens:
                    start=opens.pop()
                    maxLength = max(maxLength,i-start+1)
                else:
                    latest = i
                    break
        start = opens.pop()+1 if opens else 0
        end = latest if latest>0 else len(s)
        pdb.set_trace()
        return maxLength
        
# import pdb
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         def loop(s):
#             print(s)
#             def isValid(i):
#                 curr = []
#                 original = i
#                 while i<len(s):
#                     if not curr:
#                         original=i
#                     char = s[i]
#                     if char == '(': #open
#                         curr.append(char)
#                     else: #close
#                         if curr:
#                             curr.pop()
#                         else:
#                             return i
#                     i+=1
#                 if not curr:
#                     return i
#                 return original
#             maxLength = 0
#             i = 0
#             while i<len(s):
#                 currEnd = isValid(i)
#                 print("end: %d, start: %d"%(currEnd,i))
#                 if (currEnd-i)>maxLength:
#                     maxLength = currEnd-i
#                 i = currEnd
#                 i+=1
#             if maxLength%2==1: #BS
#                 return maxLength-1
#             return maxLength
#         a = loop(s)
#         # Reverse S, since I don't consider (
#         reverse = ""
#         for i in range(len(s)):
#             reverse += ')' if s[i]=='(' else '('
#         s = reverse[::-1]
#         b = loop(s)
#         pdb.set_trace()
#         return min(a,b)
Solution().longestValidParentheses(")()())")
Solution().longestValidParentheses(")(((((()())()()))()(()))(")