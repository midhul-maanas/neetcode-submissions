class Solution:
    def isHappy(self, n: int) -> bool:
        res = 0
        x = []
        while n:
            ch = [int(x)**2 for x in str(n)]
            res = sum(ch)
            print(f"CH:{ch} res:{res}")
            if res == 1 or res in x:
                break
            else:
                x.append(res)
            n = res
        return res == 1