class Solution:
    def hammingWeight(self, n: int) -> int:
        def ham(n, r):
            print("n: %d, r: %d"%(n,r))
            # Base
            if n==0:
                return r
            if n==1:
                return r+1
            # Recurrance
            if n%2==1:
                return ham(n//2, r+1)
            else:
                return ham(n//2, r)
        return ham(n, 0)
Solution().hammingWeight(11)
#### O(log n), O(1); 12, 100 Python3
#### TODONE: Can be constant, what exactly is constant? | Constant requires fixed-length int
#### Yay tail recursion!

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
#### Another log n solution. 41, 100 Python3