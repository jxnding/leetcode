class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = [-1]*len(heights) ####
        for i in range(1, len(heights)):
            l = i-1
            while l>=0 and heights[l]>=heights[i]:
                l = left[l]
            left[i] = l
        right = [len(heights)]*len(heights)
        for i in range(len(heights)-2, -1, -1):
            r = i+1
            while r<len(heights) and heights[r]>=heights[i]:
                r = right[r]
            right[i] = r
        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, heights[i]*(right[i]-left[i]-1))
        return max_area
#### O(n), O(n); 16, 9 Python3
# REVIEW
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            l, r = i, i
            for j in range(i-1, -1, -1):
                # Bottleneck
                if heights[j] < heights[i]: 
                    l = j + 1
                    break
                l = j
            for j in range(i+1, len(heights)):
                # Bottleneck
                if heights[j] < heights[i]: 
                    r = j - 1
                    break
                r = j
            area = (r - l + 1) * heights[i]
            max_area = max(max_area, area)
        return max_area
#### O(n^2), O(1); TLE
#### TODO: Not optimal!