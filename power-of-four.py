class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num<=0: return False
        a = bin(num).split('1')
        if len(a)==2 and len(a[-1])%2==0: return True
        return False
#### TODO: Runtime
#### 45, 100 Python3
#### O(1) if int's are fixed size, else O(log n)