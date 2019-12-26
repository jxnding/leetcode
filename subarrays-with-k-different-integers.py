class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def backTrack(s, e):
            nonlocal distinct
            start, end = s, e
            start += 1
            while start<end:
                curr = set(A[start:end])
                if len(curr)==K:
                    distinct+=1
                elif len(curr)<K: break
                start+=1

        distinct = 0
        start, end = 0, 1
        while end<=len(A):
            curr = set(A[start:end])
            if len(curr)==K: #enough distinct
                backTrack(start,end)
                distinct+=1
                end+=1
                # start+=1
            elif len(curr)>K: #too much
                start+=1
            else: #not enough
                end+=1
        return distinct
#### TODO: TLE rn. Should be O(n)?