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