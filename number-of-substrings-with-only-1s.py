class Solution:
    def numSub(self, s: str) -> int:
        """     
        1 1,1
        11 2,3
        111 3,6
        1111 4,10
        11111 5,15
        111111 6,21
        1111111 7,28

        (n+0.5)^2//2
        """
        def substrings(n):
            return (n+0.5)**2//2

        ans = 0
        currLen = 0
        for char in s:
            if char == '1':
                currLen += 1
            else:
                ans += substrings(currLen)
                currLen = 0
        ans += substrings(currLen)
        
        return int(ans % (10**9+7))
