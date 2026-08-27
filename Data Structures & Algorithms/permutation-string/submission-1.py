class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        for i in s1:
            s1Count[i] = 1 + s1Count.get(i,0)
        print(f"s1Count: {s1Count}")
        l,r = 0,len(s1)-1
        while r < len(s2):
            s2Count = {}
            for j in s2[l:r+1]:
                s2Count[j] = 1 + s2Count.get(j,0)
            print(f"s2Count: {s2Count}")
            if s1Count == s2Count:
                return True      
            l += 1
            r += 1
        return False