class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.res = []
        self.org_dist = [(math.sqrt((0 - point[0])**2 + (0 -  point[1])**2), point[0], point[1]) for point in points]
        heapq.heapify(self.org_dist)

        for i in range(k):
            dist, x, y = heapq.heappop(self.org_dist)
            self.res.append([x,y])
        
        return self.res