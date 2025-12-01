class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        Kinda like prefix sum? We figure out target (just (sum(nums) - p) % p), then loop through and find shortest array that gets that
        prefix tracks the latest index of a sum?
        Special case for n == target

        Runtime
73ms
Beats72.70%
Memory
38.14MB
Beats57.10%
        """
        prefix = {0: -1}
        target = sum(nums) % p
        # print(target)
        if target == 0: return 0
        ans = 1000000000000
        currSum = 0
        for i, n in enumerate(nums):
            currSum = (currSum + n) % p
            # print(prefix)
            # print(currSum)
            if (currSum-target) % p in prefix:
                # print('boom')
                ans = min(ans, i-prefix[(currSum-target) % p])
            # if target == n: #special case because prefix[0] is not init'd
            #     return 1
            prefix[currSum] = i
        if ans == len(nums): return -1
        if ans == 1000000000000: return -1
        return ans

# {6: 0}
# {6: 0, 0: 1}
# {6: 0, 0: 1, 5: 2}
# {6: 0, 0: 1, 5: 2, 7: 3}
