class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(points)
        d = []
        ans = []

        def caldisc(x,y):
            return math.sqrt((x**2) + (y**2))

        for i, p in enumerate(points):
            a,b = p[0],p[1]
            d.append((caldisc(a,b), i))

        heapq.heapify(d)

        while k > 0:
            ans.append(points[heapq.heappop(d)[1]])
            k -= 1


        return ans






        

        

