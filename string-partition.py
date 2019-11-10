# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# Note:

# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
import pdb
class Solution:
    def partitionLabels(self, S):
        start = {}
        end = {}
        for i, char in enumerate(S):
            if char in start:
                end[char]=i
            else:
                start[char]=i
                end[char]=i
        
        # create ranges
        ranges=[]
        curr = (0,0)
        for key in start:
            if start[key]<=curr[1]: #overlap
                curr = (curr[0], max(end[key],curr[1]))
            else:
                ranges.append(curr)
                curr = (start[key], end[key])
        ranges.append(curr)
        # answer
        ans = []
        for r in ranges:
            ans.append(r[1]-r[0]+1)
        return ans
print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
