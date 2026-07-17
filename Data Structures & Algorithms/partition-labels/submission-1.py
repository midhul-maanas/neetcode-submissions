class Solution:
    def partitionLabels(self, s):
        h = {}
        for i in range(len(s)):
            h[s[i]] = i
        print(h)
        size,end = 0,0
        res = []
        for i in range(len(s)):
            end = max(h[s[i]],end) 
            size += 1
            if i == end:
                res.append(size)
                size = 0
        return res