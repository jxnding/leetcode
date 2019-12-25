class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def checkRepeat(i):
            a, b = 0, 0
            while b<len(s):
                if s[a]!=s[b]: return False
                a += 1
                b += 1
                if a==i: a = 0
            if a==0: return True
            return False
        for i in range(1, len(s)//2+1):
            if len(s)%i!=0: continue
            if checkRepeat(i): return True
        return False
#### O(n^2), O(1); 5, 100 Python3; 18, 75 Python2
