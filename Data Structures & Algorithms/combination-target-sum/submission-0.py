class Solution:
    def combinationSum(self,nums: List[int], target: int,i = 0, s = 0, res =None,sub = None) -> List[List[int]]:
        if res == None: res = []
        if sub == None: sub = []
        if i == len(nums):
            if target == 0:
                res.append(sub[:])
            return res
        if nums[i] <= target:
            sub.append(nums[i])
            self.combinationSum(nums,target - nums[i],i,s + nums[i],res,sub)
            sub.pop()
        self.combinationSum(nums,target,i+1,s,res,sub)
        return res