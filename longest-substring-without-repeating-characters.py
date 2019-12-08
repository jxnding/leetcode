class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        d = {}
        start = 0
        for i,c in enumerate(s):
            if c in d:
                if d[c]>=start: #careful
                    ans = max(ans, i-start) #store substring length
                    start=d[c]+1 #reset start
                    d[c]=i #reset dict index
                else:
                    d[c]=i
            else:
                d[c]=i
        ans = max(ans, len(s)-start)
        return ans
#### O(n), O(n); 97; 100 Python3

#### Below is from 10/25
#### My new solution is faster!!!!
#### 11; 99 Python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        currMax = 0
        m = 0
        
        i = 0
        # for i in range(0, len(s)):
        while i<len(s):
            if s[i] in chars:
                currMax = max(currMax,i-m)
                i = chars[s[i]]+1
                chars = {}
                chars[s[i]] = i
                m = i
            else:
                chars[s[i]] = i
            i+=1 
        currMax = max(currMax,len(s)-m)
        return currMax
