class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # n = len(tasks)
        freq = Counter(tasks)
        pq = [-ele for ele in freq.values()]
        # print(pq)
        heapq.heapify(pq) #max heap

        q = deque()
        time = 0

        while pq or q:

            time += 1

            if pq:
                cnt = heapq.heappop(pq)
                cnt += 1 #since we stored negative values in the heap

                if cnt:
                    q.append((cnt,time+n))

            if q and q[0][1] == time:
                heapq.heappush(pq, q.popleft()[0])

        return time

