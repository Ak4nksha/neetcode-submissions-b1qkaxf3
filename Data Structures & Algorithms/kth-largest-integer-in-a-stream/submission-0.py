class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        self.n = len(self.heap)
        while self.n > self.k:
            heapq.heappop(self.heap)
            self.n -= 1
        
    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)
        self.n += 1
        if self.n > self.k:
            heapq.heappop(self.heap)
            self.n -= 1

        return self.heap[0]

        


        
