class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for n in nums:
            if count==0:
                candidate=n
                count+=1
            elif n==candidate:
                count+=1
            else:
                count-=1
        return candidate
#### 1 clap! O(n) and O(1)
#### Optimal!