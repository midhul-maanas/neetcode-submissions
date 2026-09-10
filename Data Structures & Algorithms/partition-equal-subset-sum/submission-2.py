class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1: #odd nums check
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2 

        for i in nums:
            newDP = dp.copy()
            for j in dp:
                #dp.add(i+j) not possible. so we need new set or copy(newDP).
                newDP.add(i+j)
            dp = newDP
            if target in dp:
                return True
        return False