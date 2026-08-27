class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0] * 26
        for i in s1:
            s1Count[ord(i) - ord('a')] += 1
        print(f"s1Count: {s1Count}")
        l,r = 0,len(s1)-1
        s2Count = [0] * 26
        for j in s2[l:r+1]:
            s2Count[ord(j) - ord('a')] += 1
        
        while r < len(s2):          
            print(f"s2Count: {s2Count}")
            if s1Count == s2Count:
                return True      
            r += 1
            if r < len(s2):
                s2Count[ord(s2[l]) - ord('a')] -= 1
                s2Count[ord(s2[r]) - ord('a')] += 1
                l += 1
            
        return False