class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,n = 0,len(s)
        maxLen = 0
        visited = set()
        for r in range(n):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            maxLen = max(maxLen,r-l+1)
        return maxLen