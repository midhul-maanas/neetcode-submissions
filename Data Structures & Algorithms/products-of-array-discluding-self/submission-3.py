from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)
        for i in range(len(nums)):
            newNum = nums[:i]+nums[i+1:]
            out[i] = reduce(lambda x,y:x*y,newNum) if newNum else 0
        return out