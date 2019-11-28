class Solution:
    def isValid(self, s: str) -> bool:
        # Match info
        match = {}
        match['}']='{'
        match[']']='['
        match[')']='('
        #Edge cases
        if s==None:
            return False
        if s=="":
            return True
        if s[0] not in match.values():
            return False
        
        curr = ""
        for char in s:
            if char in match.values(): #open
                curr+=char
            elif char in match:
                if len(curr)>0 and curr[-1]==match[char]:
                    curr=curr[:-1] #need to optimize...
                else:
                    return False
        if curr=="":
            return True
        return False
#### Yep, O(n) and O(n). But my solution should use a stack...

#### I am retarded
# class Solution:
#     def isValid(self, s: str) -> bool:
#         # Match info
#         match = {}
#         match['}']='{'
#         match[']']='['
#         match[')']='('
#         #Edge cases
#         if s==None:
#             return False
#         if s=="":
#             return True
#         if s[0] not in match.values():
#             return False
#         #initialize counter
#         counter = {}
#         counter["{"]=0
#         counter["["]=0
#         counter["("]=0
        
#         #Check validity
#         lastBracket = 0
#         counter[s[0]]+=1
#         for i in range(1,len(s)):
#             char = s[i]
#             if char in ["{","[","("]:
#                 counter[char]+=1
#                 lastBracket=i
#             elif char in ["}","]",")"]:
#                 if match[char]==s[lastBracket]:
#                     lastBracket-=1
#                     counter[match[char]]-=1
#                 else:
#                     return False
#             else:
#                 return False
            
#         return counter["{"]==counter["["]==counter["("]==0