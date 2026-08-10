class Solution:
    def permute(self, nums: List[int],i=0,res=None,sub=None) -> List[List[int]]:
        if res == None: res = []
        if sub == None: sub = nums
        
        if i == len(nums):
            print(sub)
            res.append(sub[:])
            return res
        # sub[0],sub[i] = sub[i],sub[0]
        # self.permute(nums,i+1,res,sub)
        for j in range(i,len(nums)):
            sub[i],sub[j] = sub[j],sub[i]
            self.permute(nums,i+1,res,sub)
            sub[i],sub[j] = sub[j],sub[i]
        return res