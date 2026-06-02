class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        s1 = [ch for ch in s]
        for i in range(len(t)):
            if not (t[i] in s1):
                return False
            else:
                s1.remove(t[i])
        return True
