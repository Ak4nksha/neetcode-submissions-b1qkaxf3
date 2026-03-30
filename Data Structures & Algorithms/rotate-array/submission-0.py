class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        count = 0
        start = 0


        while(count<n):
            curr = start
            prev = nums[start]

            while True:
                next = (curr + k)%n
                # can't do swapping because you are moving elements in two direction
                #nums[curr],nums[next] = nums[next],nums[curr] 
                #that's why we need a temp or prev variable to store the values

                prev, nums[next] = nums[next], prev
                curr = next
                count += 1

                if curr == start:
                    break

            start += 1