class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles) #range of k. max(piles) since if koko can eat at max(piles) then he can eat all the other piles in 1 hour
        res = r
        while l <= r:
            k = (l+r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
            
            