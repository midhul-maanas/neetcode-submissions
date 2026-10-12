class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        c = 0
        for i in range(1,len(height)):
            if height[i-1] >= c:
                c = height[i-1]
            maxL[i] = c
        maxR = [0] * len(height)
        c = 0
        for i in range(len(height)-2,-1,-1):
            if height[i + 1] >= c:
                c = height[i+1]
            maxR[i] = c
        water = 0
        for i in range(len(height)):
            if min(maxL[i],maxR[i]) - height[i] >= 0:
                water += min(maxL[i],maxR[i]) - height[i]
        return water
