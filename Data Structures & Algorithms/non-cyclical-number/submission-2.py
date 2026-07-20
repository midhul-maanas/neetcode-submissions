class Solution:
    def isHappy(self, n: int) -> bool:
        res = 0
        s = set()
        while n:
            ch = [int(x)**2 for x in str(n)]
            res = sum(ch)
            print(f"CH:{ch} res:{res}")
            if res == 1 or res in s:
                break
            else:
                s.add(res)
            n = res
        return res == 1