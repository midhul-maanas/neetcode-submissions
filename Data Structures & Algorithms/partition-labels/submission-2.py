class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = { char: i for i,char in enumerate(s) }
        res = []
        start,end = 0,0
        for i in range(len(s)):
            end = max(h[s[i]],end)
            start += 1
            if i == end:
                res.append(start)
                start = 0
        return res