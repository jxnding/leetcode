class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        long = ["" for x in range(max(len(num1),len(num2)))]
        num1, num2 = num1[::-1], num2[::-1]
        carry = 0
        for i in range(len(long)):
            # i = len(long)-k-1
            try:
                c1 = int(num1[i])
            except IndexError:
                c1 = 0
            try:
                c2 = int(num2[i])
            except IndexError:
                c2 = 0
            c = c1+c2+carry
            print("i: "+str(i)+" c1: "+str(c1)+" c2: "+str(c2)+" carry: "+str(carry))
            carry = 0
            if c>9:
                carry = 1
                c-=10
            # Assign
            print(str(c))
            long[i]=str(c)
        if carry>0:
            long = long+["1"]
        ans = ""
        for e in long:
            ans+=e
        return ans[::-1]
print(Solution().addStrings('9','99'))
#### no clap
#### n^2