from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        q = deque()
        q.append((nums[0],0,0)) #val,index,len
        l = 0
        visited = set()
        while q:
            n,currInd,l = q.popleft()
            print(f"N:{n} CURRIND: {currInd} L: {l}")
            if currInd >= len(nums) - 1:
                return l
            for i in range(currInd+1,min((n+currInd) + 1,len(nums))):
                if i not in visited:
                    visited.add(i)
                    q.append((nums[i], i ,l+1))
        return l
            