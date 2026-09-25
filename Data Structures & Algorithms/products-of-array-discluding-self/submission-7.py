class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod,zero = 1,0
        for i in nums:
            if i != 0:
                prod *= i
            if i == 0:
                zero += 1
        if zero > 1:
            return [0] * len(nums)
        for i in range(len(nums)):
            if zero:
                if nums[i] == 0:
                    nums[i] = prod
                else:
                    nums[i] = 0
            else:
                nums[i] = prod // nums[i]
            
        return nums