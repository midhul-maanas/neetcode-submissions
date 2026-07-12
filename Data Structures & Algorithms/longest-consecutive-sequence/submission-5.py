class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = sorted(set(nums));
        print(f"Sorted:{sort}")
        res = []
        c = 0
        if not sort:
            return 0
        for i in range(len(sort)-1):
            if (sort[i]+1 == sort[i+1]):
                c+=1
            else:
                res.append(c+1)
                c=0
        res.append(c+1)      
        res.sort(reverse=True)
        return res[0]