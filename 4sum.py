class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(target, start):
            complements = {}
            ans = []
            for i in range(start,len(nums)):
                n = nums[i]
                if n not in complements:
                    complements[target-n]=i
                else:
                    ans.append([complements[n], i])
                    complements[target-n]=i
            return ans
        indices = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ans = twoSum(target-nums[i]-nums[j], j+1)
                for k, l in ans:
                    quad = [i,j,k,l]
                    quad = [nums[x] for x in quad]
                    indices.append(tuple(sorted(quad)))
        # De-duplicate indices
        indices = set(indices)
        # Convert indices to numbers
        ans = []
        for quad in indices:
            ans.append(list(quad))
        return ans
#### TODO should be a error from the twoSum returning []!
#### O(n^3), O(n); 40, 100 Python3; 30, 27 Python2
#### I'm optimal!