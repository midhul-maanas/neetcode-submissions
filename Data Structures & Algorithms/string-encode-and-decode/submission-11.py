class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for i in strs:
            res.append(str(len(i)))
            res.append('#')
            res.append(i)
        return "".join(res)      

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):  
            '''5#hello5#world'''
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res