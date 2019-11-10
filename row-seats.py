import pdb
class Solution:
    def maxDistToClosest(self, seats):
        ans = [0]*len(seats)
        for i in range(len(seats)):
            if seats[i]==1: #occupied
                continue
            left, right = -1000000, 1000000
            for j in range(len(seats)):
                if seats[j]==1:
                    if j<i:
                        left = max(left,j)
                    if j>i:
                        right = min(right,j)
            ans[i]=min(right-i,i-left)
        pdb.set_trace()
        return max(ans)

print(Solution().maxDistToClosest([1,0,0,0,1,0,1]))