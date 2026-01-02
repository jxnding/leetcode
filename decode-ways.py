from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        # # Non analyitic way
        # # DFS by looking at next 2
        # # Stack of indices (so we don't have to change the string)
        # CODES = set([str(x) for x in range(1,27)])

        # ans = 0
        # stack = [0]
        # while len(stack) > 0:
        #     currIdx = stack.pop()
        #     # if currIdx < len(s)-1: # need 1 lookforward
        #     #     # if can be decoded separately (2 singletons), let's just worry about first one
        #     #     if s[currIdx] in CODES:
        #     #         stack.append
        #     #     # if can be decoded together (1 dualton)
        #     #     if s[currIdx] + s[currIdx+1] in CODES:
        #     # else: #on the last char
        #     #     if s[currIdx] in CODES:
        #     if currIdx == len(s):
        #         ans += 1
        #         continue
        #     if currIdx < len(s)-1: # can do 2
        #         if s[currIdx] + s[currIdx+1] in CODES:
        #             stack.append(currIdx+2)
        #     if s[currIdx] in CODES:
        #         stack.append(currIdx+1)
        # # TODO: can optimize dead-ends
        # return ans

        ########### DP recursion w/ cache
        # # Can either cache but have everything on stack (can't do tail recursion) OR can have nonlocal optimization
        # @cache
        # def numWays(idx):
        #     # nonlocal ans
        #     if idx == len(s):
        #         # ans += 1
        #         # return
        #         return 1
        #     ans = 0
        #     if idx < len(s)-1:
        #         if s[idx] + s[idx+1] in CODES:
        #             # numWays(idx+2)
        #             ans += numWays(idx+2)
        #     if s[idx] in CODES:
        #         # numWays(idx+1)
        #         ans += numWays(idx+1)
        #     return ans
            
        # CODES = set([str(x) for x in range(1,27)])
        # # ans = 0
        # # numways(0)
        # ans = numWays(0)
        # return ans

        ########### DP bottom up
        CODES = set([str(x) for x in range(1,27)])
        dp = [1] # 1 for the '' empty string
        dp += [0 for _ in s]
        # dp[1] = 1 if s[0] in CODES else 0
        if s[0] in CODES:
            dp[1] = 1
        else:
            return 0
        for i in range(1, len(s)):
            if s[i-1] + s[i] in CODES:
                dp[i+1] += dp[i-1]
            if s[i] in CODES:
                # dp[i] += 1
                dp[i+1] += dp[i]
            if s[i-1] + s[i] not in CODES and s[i] not in CODES:
                return 0
        return dp[-1]