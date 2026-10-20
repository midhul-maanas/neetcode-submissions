class Solution:
    def countBits(self, n: int) -> List[int]:
        i = 0
        res = [0] *(n + 1)
        while i <= n:
            num = i
            while num:
                res[i] += 1 if num & 1 else 0
                num >>= 1
            i += 1
        return res

           
        

                