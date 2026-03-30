class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minheap = [nums[0]]
        heapq.heapify(minheap)

        
        for ele in nums[1:]:

            heapq.heappush(minheap, ele)

            if len(minheap) > k:
                heapq.heappop(minheap)

        
        return minheap[0]