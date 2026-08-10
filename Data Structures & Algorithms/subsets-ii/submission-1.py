class Solution:
    def subsetsWithDup(self, nums: List[int],i = 0,sub = None ,res =None) -> List[List[int]]:
        if sub == None: sub = []
        if res == None: res = []
        nums.sort()
        if i == len(nums):
            res.append(sub[:])
            return res
        sub.append(nums[i])
        self.subsetsWithDup(nums,i+1,sub,res)
        sub.pop()
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        self.subsetsWithDup(nums,i+1,sub,res)
        return res