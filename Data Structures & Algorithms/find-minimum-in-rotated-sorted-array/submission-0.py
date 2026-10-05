class Solution:
    def findMin(self, nums: List[int]) -> int:
        #O(n)
        m = nums[0]
        for i in range(1,len(nums)):
            m = min(m,nums[i])
        return m