from functools import cache
class Solution:
    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # OK, dp can be done in 3 ways:
        #   recursive
        #   recursive w/ cache a.k.a. top-down
        #   bottom-up
        
        # Base cases
        if s3 == '' and s2 == '' and s1 == '': return True
        if s3 == '': return False

        # Recursion
        endOnS1 = False
        if s1 and s3[-1] == s1[-1]:
            endOnS1 = self.isInterleave(s1[:-1], s2, s3[:-1])
        endOnS2 = False
        if s2 and s3[-1] == s2[-1]:
            endOnS2 = self.isInterleave(s1, s2[:-1], s3[:-1])
        return endOnS1 or endOnS2
# Beats 59% and 6%


