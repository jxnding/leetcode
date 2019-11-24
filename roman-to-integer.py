class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            }
        if len(s)==0: return 0
        if len(s)==1: return value[s]
        
        ans = 0
        for i in range(len(s)-1):
            a, b = s[i],s[i+1]
            if a=='I' and (b=='V' or b=='X'):
                ans-=value[a]
            elif a=='X' and (b=='L' or b=='C'):
                ans-=value[a]
            elif a=='C' and (b=='D' or b=='M'):
                ans-=value[a]
            else:
                ans+=value[a]
        ans+=value[b]
        return ans
#### O(n), O(1)
#### 1 clap!
