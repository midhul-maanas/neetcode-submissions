class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        v = set()
        longest = 0
        for i in nums:
            v.add(i)
        v = sorted(list(v))
        print(sorted(v))
        i,j = 0,1
        c = 1
        while i < len(v) and j < len(v):
            if v[j] == v[i] + 1:
                c += 1
            else:
                c = 1
            longest = max(longest,c)
            i = j
            j += 1
            
        return max(longest,c)

            

            


        
            