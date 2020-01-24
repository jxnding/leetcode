class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def ones(num, counter):
            counter = 0
            while num:
                num &= num-1
                counter+=1
            return counter
        return ones((x^y),0)