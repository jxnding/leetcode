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