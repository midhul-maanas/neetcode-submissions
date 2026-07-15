class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums) 
        curr,prev = 0,0
        for i in nums:
            temp = curr
            curr = max(curr,prev + i)
            prev = temp
        return curr