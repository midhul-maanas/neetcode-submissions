class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()      
        res = []
        for i in range(len(nums)):#pivot
            if i > 0 and nums[i] == nums[i - 1]: #duplicate skipping
                continue
            l,r = i + 1,len(nums) - 1
            while l < r:
                x = -nums[i]
                s = nums[l] + nums[r]
                if s < x:
                    l += 1
                elif s > x:
                    r -= 1
                else:
                    res.append([nums[l],nums[r],nums[i]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:#duplicate skipping
                        l += 1
                    r -= 1
                    while r > 0 and nums[r] == nums[r + 1]:#duplicate skipping
                        r -= 1
        return res
