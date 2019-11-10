class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if not (rec2[0]>=rec1[2] or rec2[2]<=rec1[0]): # x overlap
            if not (rec2[1]>=rec1[3] or rec2[3]<=rec1[1]): # y overlap
                return True
        return False