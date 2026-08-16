class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_heap, res = [], []
        for x, y in points:
            heapq.heappush(points_heap, (math.sqrt(x**2+y**2), x, y))
        for i in range(k):
            _, x, y = heapq.heappop(points_heap)
            res.append([x,y])
        return res