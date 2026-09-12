class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i,f = len(nums) - 1,len(nums) - 1
        while i >= 0 and f > 0:
            if i + nums[i] >= f:
                f = i
            i -= 1
        return f == 0