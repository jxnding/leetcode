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