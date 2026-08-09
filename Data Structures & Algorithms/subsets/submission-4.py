class Solution:
    def subsets(self,nums: List[int],i=0,sub = None,res = None) -> List[List[int]]:
        if sub == None: sub = []
        if res == None: res = []
        if i == len(nums):
            res.append(sub.copy())
            return res
        sub.append(nums[i])
        self.subsets(nums,i+1,sub,res)
        sub.remove(nums[i])
        self.subsets(nums,i+1,sub,res)
        return res