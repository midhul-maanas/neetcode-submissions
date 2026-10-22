class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [ -n for n in stones ]
        heapq.heapify(maxHeap)
        while len(maxHeap) >= 2:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            if x > y:
                heapq.heappush(maxHeap,-(x-y))
            elif y > x:
                heapq.heappush(maxHeap,-(y-x))
        return abs(maxHeap[0]) if maxHeap else 0   