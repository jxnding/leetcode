class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return nums[0]

        #populate initial list, start = 0, end is variable
        products = [0]*N
        products[0] = nums[0]
        for end in range(1,N):
            products[end] = products[end-1] * nums[end]
        max_product = max(products)

        #divide out the starts, starting with start = 1
        for start in range(N):
            for i in range(start+1,N): #because start >= end
                # None is a skip from a divide by zero
                if products[i] == None: 
                    products[i] = nums[i]
                    max_product = max(max_product, products[i])
                    continue
                try:
                    products[i] = products[i] // nums[start]
                    max_product = max(max_product, products[i])
                except ZeroDivisionError:
                    products[i] = nums[i] #not None? we actually don't know because we wiped it
        return max_product
