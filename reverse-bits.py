class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n,'#034b')[:1:-1],2)
#### O(log n), O(log n); 51, 100 Python3