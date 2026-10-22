class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        for p in points:
            dist = math.sqrt(p[0]**2+p[1]**2)
            heapq.heappush(minHeap,[dist,p[0],p[1]])
        res = []
        for i in range(k):
            c = heapq.heappop(minHeap)
            x,y = c[1],c[2]
            res.append([x,y])
        return res