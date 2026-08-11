class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(sub,oc,cc):
            if len(sub) == 2*n:
                res.append(sub)
                return 
            if oc < n:
                backtrack(sub+"(",oc+1,cc)
            if cc < oc:
                backtrack(sub+")",oc,cc+1)
        backtrack("",0,0)
        return res