# from queue import PriorityQueue
import heapq
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # def findMinPositive():
        #     minVal, minLoc = 100000000000000, None
        #     for i in range(len(nums)):
        #         if nums[i] == 0: continue
        #         if nums[i] < minVal:
        #             minVal, minLoc = nums[i], i
        #     return minVal, minLoc
        
        # def binarySearch(x, target):
        #     L, R = 0, len(x)
        #     while L < R:
        #         mid = (L + R) // 2
        #         if x[mid] > target:
        #             R = mid - 1
        #         elif x[mid] < target:
        #             L = mid + 1
        #         else:
        #             return mid
        #     assert L == R
        #     return L

        # def expand(start):
        #     nonlocal zeroInd
        #     # L = 0
        #     # for i in range(start, -1, -1):
        #     #     if nums[i] == 0:
        #     #         L = i + 1
        #     #         break
        #     #     # L = i
            
        #     # R = len(nums) - 1
        #     # for i in range(start, len(nums)):
        #     #     if nums[i] == 0:
        #     #         R = i - 1
        #     #         break
        #     #     # R = i
        #     # return L, R
        #     startLoc = binarySearch(zeroInd, start)
            
        
        # def operation(minVal, l, r):
        #     nonlocal operations
        #     nonlocal zeroInd
        #     for i in range(l, r + 1):
        #         if nums[i] == minVal:
        #             nums[i] = 0
        #             # Add to zeroInd
        #             insertLoc = binarySearch(zeroInd, i)
        #             zeroInd.insert(insertLoc, i)
        #             operations -= 1

        # # grab min positive item
        # # expand until we get a 0
        # # apply operation

        # # can't do " while minVal != originalMaxVal:" because you might have to operate on that several times
        # ## Optimize while loop
        # ## Optimize expansion (build sorted list of zero-indices, bin search that)

        # ## Build zero-indices
        # zeroInd = []
        # for i, val in enumerate(nums):
        #     if val == 0: zeroInd.append(i)
        

        # operations = sum([x > 0 for x in nums])
        
        # ans = 0
        # originalMaxVal = max(nums)
        # minVal = 10000000000000000000
        # # while sum(nums) > 0: #TODO: optimize?
        # # while minVal != originalMaxVal:
        # while operations != 0:
        #     minVal, minLoc = findMinPositive()
        #     l, r = expand(minLoc)
        #     operation(minVal, l, r)
        #     ans += 1
        # return ans
############## 
        # if sum(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return 1
        
        # ans = 1
        # if nums[0] == 0:
        #     ans = 0
        # for i in range(1, len(nums)):
        #     if nums[i] > nums[i-1]:
        #         ans += 1
        #     elif nums[i] < nums[i-1]:
        #         pass #ok to go down
        #     else:
        #         pass
        
        # return ans
########### PQ
        # while pq
            # get max
            # expand (== only)
        
        # if sum(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return 1

        # # Deduplicate
        # numsDistinct = [nums[0]]
        # for i in range (1, len(nums)):
        #     if nums[i] != numsDistinct[-1]:
        #         numsDistinct.append(nums[i])

        # pq = []
        # for i, n in numsDistinct:
        #     heapq.heappush(pq, (-n, i, i)) # sort by index second to be stable
        
        # ans = 1
        # (currVal, currInd, _ ) = heapq.heappop(pq)
        # while pq:
            
########### monotonic stack... after i looked
        ans = 0
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] < stack[-1]:
                stack.pop()
                ans += 1
            if stack and nums[i] == stack[-1]:
                pass
            else:
                stack.append(nums[i])
        # while stack and stack[-1] > 0:
        #     stack.pop()
        #     ans += 1
        ans += len(stack)
        if stack[0] == 0: ans -= 1
        return ans
            # if nums[i] > stack[-1]:
            #     stack.append(nums[i])
            # if nums[i] < stack[-1]:


