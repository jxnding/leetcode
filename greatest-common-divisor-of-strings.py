class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            if b==0: return a
            return gcd(b, a%b)
        s1 = str1+str2
        s2 = str2+str1
        if s1==s2:
            return s1[:gcd(len(str1), len(str2))]
        return ""
#### O(n), O(n); 95, 100
#### James is smart