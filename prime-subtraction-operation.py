import math
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def sieve(n):
            primes = [True] * (n+1) #fastest way?
            for i in range(2, math.ceil(math.sqrt(n))+1):
                j = 2*i
                while j <= n:
                    primes[j] = False
                    j += i
            primes[0] = False #0 is not prime
            primes[1] = False #1 is not prime
            return primes
        def binary_search(nums, s, e, t, last = -1):
            if e < s: return False, last #return last checked number 
            mid = (s+e)//2
            mid_num = nums[mid]
            if mid_num == t:
                return True, mid
            elif mid_num < t:
                return binary_search(nums, mid+1, e, t, mid) ## could be here too 
            else:
                return binary_search(nums, s, mid-1, t, mid)
        # Calculate all primes smaller than the max number m; O log log m time + m space.
        max_num = max(nums)
        primes = sieve(max_num)
        # primes = [n if primes[n] for n in range(len(primes))]
        p = []
        for i in range(len(primes)):
            if primes[i]: p.append(i)
        # Can array be made strictly decreasing?
        for i in range(len(nums)-1):
            # Calculate target (maximum we can subtract while maintaining nums[i]>nums[i-1])
            if i == 0:
                target = nums[i]
            else:
                target = nums[i] - nums[i-1]
            # Find max prime < target
            res, prime_ind = binary_search(p, 0, len(p)-1, target)
            # Subtract prime from thing
            if res: #subtract biggest prime LESS THAN number
                if prime_ind > 0: #Python allows -1 indexing
                    nums[i] -= p[prime_ind-1]
            else:
                if p[prime_ind] > target and prime_ind > 0:
                    nums[i] -= p[prime_ind-1]
                elif p[prime_ind] < target:
                    nums[i] -= p[prime_ind]
            if nums[i] >= nums[i+1]:
                return False #we can't make the next number bigger, and we've already taken the max out of the current
        return True