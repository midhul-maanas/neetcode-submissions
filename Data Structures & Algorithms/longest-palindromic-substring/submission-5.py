class Solution:
    def longestPalindrome(self, s: str) -> str:
      n = len(s)
      maxLen = 0
      longPal = ""
      for i in range(n):
        #odd length string
        l,r = i,i
        while l >= 0 and r < n and s[l] == s[r]:
          if (r-l+1) > maxLen:
            maxLen = r-l+1
            longPal = s[l:r+1]
          l -= 1
          r += 1

        #even length string
        l,r = i,i+1
        while l >= 0 and r < n and s[l] == s[r]:
          if (r-l+1) > maxLen:
            maxLen = r-l+1
            longPal = s[l:r+1]
          l -= 1
          r += 1
      return longPal