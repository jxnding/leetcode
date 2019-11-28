class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        b = []
        for e in arr:
            if e==0:
                b.append(0)
                b.append(0)
            else:
                b.append(e)

        for i in range(len(arr)):
            arr[i]=b[i]
        
