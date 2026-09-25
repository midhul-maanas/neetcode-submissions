class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i,j = 0,1
        # while i < len(nums):
        #     if j == len(nums):
        #         i += 1
        #         j = i + 1
        #     if nums[i] + nums[j] == target:
        #         return [i,j]
        #     else:
        #         j += 1
        h = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in h:
                return [h[difference],i]
            else:
                h[nums[i]] = i
        
