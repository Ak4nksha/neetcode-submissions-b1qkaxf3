from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        d = {}
        d2 = defaultdict(list)
        ans = []

        for ele in nums:
            if ele in d:
                d[ele] += 1
            else:
                d[ele] = 1

        for ele,cnt in d.items():
            d2[cnt].append(ele)

        for i in range(n,-1,-1):

            if i in d2:
                for ele in d2[i]:
                    if k == 0:
                        break
                    ans.append(ele)
                    k -= 1
                    # if k == 0:
                    #     break
        return ans
            




        
        
