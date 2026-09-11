class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        for i in range(n):
            dp[i] = max(nums[i],dp[i-1] + nums[i])
        print(dp)
        return max(dp)