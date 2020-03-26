class Solution:
    def myPow(self, x: float, n: int) -> float:
        b = bin(abs(n))[2:]
        ans, x_val = 1, x
        for i in range(len(b)-1,-1,-1):
            if b[i]=='1':
                ans *= x_val
            x_val *= x_val
        if n<0: return 1/ans
        return ans
#### O(log n), O(1); 88, 100 Python3; 42, 12 Python2
#### REVIEW

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         ans = 1
#         for _ in range(abs(n)):
#             ans *= x
#         if n < 0: return 1/ans
#         return ans
# #### O(n), O(1); TLE
