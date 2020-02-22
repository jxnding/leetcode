class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        longest = [{}]
        max_length = 1
        for i in range(1,len(A)):
            i_longest = {}
            for j in range(i):
                interval = A[i]-A[j]
                curr_length=longest[j][interval]+1 if interval in longest[j] else 2
                # if interval in i_longest:
                max_length = max(max_length, curr_length)
                i_longest[interval] = curr_length
            longest.append(i_longest)
        return max_length
#### O(n^2), O(n^2); 84, 91 Python3; 94, 91 Python
#### {}.get() is super useful!