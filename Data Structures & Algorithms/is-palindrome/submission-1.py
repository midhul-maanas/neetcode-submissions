class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch for ch in s if ch.isalnum())
        cleanS = "".join(s.split())
        revS = cleanS[::-1]
        return cleanS.lower() == revS.lower()