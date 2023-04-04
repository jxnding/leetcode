class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # average_int = round(sum(nums)/len(nums))
        # return sum([abs(n - average_int) for n in nums])
##
        # N, D = sum(nums), len(nums) #store avg as fraction to avoid fp imprecision
        # ans = []
        # for q in queries:
        #     QD = q * D
        #     diffD = abs(N - QD)
        #     ans.append(diffD * N // D)
        # return ans
##
        average = sum(nums)/len(nums)
        ans = []
        for q in queries:
            ans.append(round(abs(average-q)*len(nums)))
        return ans

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # calculate "variance" against the first query
        V = sum([abs(n - queries[0]) for n in nums])
        ans = [V]

        # calculate all other min costs as constant time operations
        for i in range(1, len(queries)):
            ans.append(abs(queries[0]-queries[i]) * len(nums))
        
        return ans

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # calculate "variance" against the mean
        U = sum(nums)/len(nums)
        V = sum([abs(U - n) for n in nums])
        # ans = [V]
        ans = []
        # calculate all other min costs as constant time operations
        for i in range(0, len(queries)):
            ans.append(V + abs(U-queries[i]) * len(nums))
        
        return ans