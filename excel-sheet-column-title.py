class Solution:
    def convertToTitle(self, n: int) -> str:
        def convert26(n):
            n -= 1
            if n < 26: return [n]
            return [n%26] + convert26(n//26)
        n = convert26(n)[::-1]
        # Convert to Excel
        offset = ord('A')
        for i in range(len(n)):
            n[i] = chr(n[i]+offset)
        return ''.join(n)
#### O(log n), O(log n); 84, 100 Python3
#### TODO