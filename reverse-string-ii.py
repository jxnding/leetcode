class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        for i in range(0,len(s),2*k):
            if len(s)-i<k:
                first = s[i:]
                second = ""
            elif len(s)-i<2*k:
                first = s[i:i+k]
                second = s[i+k:]
            else:
                first = s[i:i+k]
                second = s[i+k:i+k+k]
            ans += first[::-1]
            ans += second
        return ans
            
            