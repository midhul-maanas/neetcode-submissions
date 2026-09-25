class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visit = set()
        for i in nums:
            if i in visit:
                return True
            else:
                visit.add(i)
        return False 