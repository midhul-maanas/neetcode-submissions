class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1
        sort = sorted(count.items(),key =lambda item:item[1],reverse=True)
        res = []
        for i in range(0,k):
            res.append(sort[i][0])
        return res
        