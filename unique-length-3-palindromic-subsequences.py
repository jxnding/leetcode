class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        For loop through with before/after list[set] and intersection
        ans is a set of tuples
        return len(ans)

        O(n^2) runtime and space
        """
        #### Build before & after sets
        ## Be careful!
        # before = [set()] * len(s)
        # after = [set()] * len(s)
        before = [set() for _ in s]
        after = [set() for _ in s]

        for i in range(len(s)):
            if i > 0: #add previous too
                before[i].add(s[i-1])
                before[i] = before[i].union(before[i-1])

        for i in range(len(s)-1, -1, -1):
            if i < len(s)-1: #add previous too
                after[i].add(s[i+1])
                after[i] = after[i].union(after[i+1])

        #### For loop
        ans = set()
        for i, c in enumerate(s):
            for commonChar in before[i].intersection(after[i]):
                palindromeTuple = (commonChar, c) #implicitly will represent (commonChar, c, commonChar)
                ans.add(palindromeTuple)
        return len(ans)
        # Instead of iterating through the string to find the center of the palindrome, try iterating through the alphabet to find the edges.