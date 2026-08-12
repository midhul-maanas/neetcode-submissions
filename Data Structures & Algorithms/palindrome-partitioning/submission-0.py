class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtracking(i,sub= []):
            if i == len(s):
                res.append(sub[:])
                return 
            for j in range(i,len(s)):
                if isPall(s[i:j+1]):
                    sub.append(s[i:j+1])
                    backtracking(j+1,sub)
                    sub.pop()
        def isPall(s):
            return s == s[::-1]
        backtracking(0)
        return res
            
            