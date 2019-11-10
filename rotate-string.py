class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        if A==B:
            return True
        for offset in range(len(A)):
            good = True
            for i in range(len(A)):
                if A[i]!=B[(i+offset)%len(B)]:
                    good = False
                    break
            if good:
                return True
        return False

# Solution has an interesting all() function
# Solution is FASTER than mine! O(n) exists in multiple ways