import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        for i in points:
            sqrt = math.sqrt(i[0]**2+i[1]**2)
            heapq.heappush(minHeap,[sqrt,i[0],i[1]])
        print(minHeap)
        res = []
        for i in range(k):
            x = heapq.heappop(minHeap)
            res.append([x[1],x[2]])
        return res

