class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(str(n) for n in digits))
        res = list(str(num+1))
        return res