class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        ans = 0
        n = len(height)
        i = 0
        j = n-1

        while i<j:

            dist = j-i

            if height[i]<height[j]:
                area = dist * height[i]
                i += 1
            else:
                area = dist * height[j]
                j -= 1
            
            ans = max(ans,area)

        return ans