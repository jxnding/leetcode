class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        for i, c in enumerate(s):
            if c in chars: chars[c] = -1
            else: chars[c] = i
        
        ans = 100000000
        for value in chars.values():
            if value==-1: continue
            ans = min(ans, value)
        
        if ans==100000000: return -1
        return ans
#### O(n), O(n); Python3 58, 100; Python2 44, 84
#### TIP: collections.Counter(s)