from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = defaultdict(int)
        for i in nums:
            h[i] += 1
        # print(h) #num,count
        freq = [ [] for i in range(len(nums) + 1) ]
        for num,count in h.items():
            freq[count].append(num)
        res = []
        for i in range(len(freq) - 1,-1,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


        
