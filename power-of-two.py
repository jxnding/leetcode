class Solution(object):
    def isPowerOfTwo(self, n):
        if n<0: return False
        return bin(n)[2:].count('1')==1
#### O(log n), O(log n); 93, 100 Python3
