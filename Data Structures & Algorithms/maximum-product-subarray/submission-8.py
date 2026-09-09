class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp = nums
        # for i in range(1,len(nums)):
        #     maxVal = max(dp[i],nums[i] * dp[i-1])
        #     minVal = min(dp[i],nums[i] * dp[i-1])
        #     dp[i] = max(maxVal,minVal)
        # # print(dp)
        # return max(dp)
        res = max(nums)
        curMax,curMin = 1,1
        for n in nums:
            temp = n * curMax
            curMax = max(temp, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(curMax,res,curMin)
        return res