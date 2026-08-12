class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        dc = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def backtrack(i,sub):
            if i == len(digits):
                res.append(sub[:])
                return 
            for ch in dc[digits[i]]:
                backtrack(i+1,sub + ch)
        backtrack(0,"")
        return res