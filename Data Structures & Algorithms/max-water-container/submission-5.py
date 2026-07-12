class Solution:
    def maxArea(self, heights: List[int]) -> int:
        print(f"Original:{heights}")
        res = 0
        for i in range(len(heights)):
            for j in range(len(heights)-1,0,-1):
                height = min(heights[i],heights[j])
                width = j-i
                newArea = height*width
                if newArea > res:
                    res = newArea
        return res
        