class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {}
        for i, n in enumerate(arr2):
            order[n]=i
        # Sort into 2 lists (in arr2 and not)
        ans = []
        rest = []
        for n in arr1:
            if n in order:
                ans.append(n)
            else:
                rest.append(n)
        # Sort both lists
        ans.sort(key=lambda x:order[x])
        rest.sort()
        return ans+rest
#### O(n log n), O(1); 99, 100 Python3
#### 1 clap!