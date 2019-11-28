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

# My previous solution 11/19/19
import pdb
class Solution:
    def gcdOfStrings(self, str1, str2):
        def divides(a, b):
            # if len(b)%len(a)!=0:
            #     return False
            i = 0
            for j in range(len(b)):
                if b[j]!=a[i]:
                    return False
                i=(i+1)%len(a)
            return True
        # find divisors for str1 and str2
        d1 = ""
        for i in range(1,len(str1)+1):
            curr = str1[:i]
            if divides(curr,str1):
                d1 = curr
            # pdb.set_trace()
        d2 = ""
        for i in range(1,len(str2)+1):
            curr = str2[:i]
            if divides(curr,str2):
                d2 = curr
        print(d1)
        print(d2)
        # find longest common substring
        ans = ""
        for i in range(min(len(d1),len(d2))):
            if d1[i]==d2[i]:
                ans+=d1[i]
            else:
                break
        return ans
Solution().gcdOfStrings('abab','ababab')