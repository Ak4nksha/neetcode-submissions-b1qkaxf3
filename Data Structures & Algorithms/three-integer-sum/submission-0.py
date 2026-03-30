class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        arr = sorted(nums)
        first = 0
        res = []

        for first in range(n-2):
            
            #skip duplicates 
            if first > 0 and arr[first] == arr[first-1]:
                continue
            second = first + 1
            last = n-1
            target = -(arr[first])

            while second < last:

                s = arr[second] + arr[last]

                if s == target:

                    res.append([arr[first],arr[second],arr[last]])

                    while second<last and arr[second] == arr[second+1]:
                        second += 1
                    while second<last and arr[last] == arr[last-1]:
                        last -= 1
                    second += 1
                    last -= 1
                elif s < target:
                    second += 1
                else:
                    last -= 1

        return res




        

