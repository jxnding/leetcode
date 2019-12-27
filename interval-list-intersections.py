class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        def overlap(A, B):
            upper = min(A[1], B[1])
            lower = max(A[0], B[0])
            if lower>upper:
                return None
            else:
                return [lower, upper]
        ans = []
        a, b = 0, 0
        while a<len(A) and b<len(B):
            o = overlap(A[a], B[b])
            if o: ans.append(o)
            if A[a][1]>B[b][1]:
                b+=1
            elif A[a][1]<B[b][1]:
                a+=1
            else:
                a+=1
                b+=1
        return ans
#### O(n^2), O(n); 93, 100 Python3
#### 