class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if x<0:
            ans = -int(str(-x)[::-1])
        else:
            ans = int(str(x)[::-1])
        if ans>2**31-1:
            return 0
        if ans<-(2**31):
            return 0
        return ans
#### 84, 100 Python3; 99, 5 Python2
# Below 11/10
class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x<0:
            neg = True
            x = abs(x)
        y = int(str(x)[::-1])
        if y>2**31:
            return 0
        if neg:
            y *= -1
        return y