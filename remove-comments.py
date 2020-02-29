class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        def DFA(c):
            nonlocal state
            nonlocal out
            if state==0:
                if c=='/':
                    state = 1
                elif c=='\n':
                    pass
                else:
                    out.append(c)
            elif state==1:
                if c=='/':
                    state = 2
                elif c=='*':
                    state = 3
                else:
                    state = 0
                    out.append('/')
                    if c!='\n':
                        out.append(c)
            elif state==2:
                if c=='\n':
                    state = 0
            elif state==3:
                if c=='*':
                    state = 4
            elif state==4:
                if c=='/':
                    state = 0
                elif c=='*':
                    state = 4
                else:
                    state = 3
        ans = []
        state, out = 0, []
        for line in source:
            for c in line:
                DFA(c)
            # \n char
            DFA('\n')
            if state!=3 and out != []:
                ans.append(''.join(out))
                out = []
        return ans
#### 39, 100 Python3

# class Solution:
#     def removeComments(self, source: List[str]) -> List[str]:
#         ans = []
#         curr_line = []
#         block, reg = False, False
#         for i, line in enumerate(source):
#             j = 0
#             while j < len(line)-1:
#                 if block:
#                     if line[j]=='*' and line[j+1]=='/':
#                         j += 1
#                         block = False
#                 elif line[j] == '/' and line[j+1] == '/':
#                     reg = True
#                     break
#                 elif line[j] == '/' and line[j+1] == '*':
#                     j += 1
#                     block = True
#                 else:
#                     curr_line.append(line[j])
#                 j += 1
#             if not block and not reg:
#                 if j==len(line)-1:
#                     curr_line.append(line[-1])
#             reg = False
#             if not block and curr_line!=[]:
#                 ans.append(''.join(curr_line))
#                 curr_line = []
#         return ans
# #### Too tedious
# #### Should I use DFA?