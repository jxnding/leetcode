class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        rising = True
        peak = 0
        for i in range(len(A)-1):
            a, b = A[i], A[i+1]
            if b>a:
                if not rising:
                    return False
            elif b<a:
                if rising:
                    rising = False
                    peak = i
            else:
                return False
        if peak==0:
            return False
        return True
