class Solution:
    def combinationSum2(self, candidates: List[int], target: int,index=0,ds=None,res =None) -> List[List[int]]:
        if ds == None: ds = []
        if res == None: res = []
        candidates.sort()
        if target == 0:
            res.append(ds[:])
            return res
        
        for i in range(index,len(candidates)):
            if i > index and candidates[i] == candidates[i-1]: continue
            if candidates[i] > target: break
            ds.append(candidates[i])
            self.combinationSum2(candidates,target-candidates[i],i+1,ds,res)
            ds.pop()
        return res