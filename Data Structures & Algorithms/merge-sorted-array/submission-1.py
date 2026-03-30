class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p = 0
        q = 0
        i = 0
        s = m+n
        temp = [0] * s

        for i in range((s)):
            
            
            print(f"i = {i} , p = {p}, q ={q} temp = {temp}")
            if p == m or q == n: break
            if nums1[p] <= nums2[q]:
                temp[i] = nums1[p]
                p += 1
            else:
                temp[i] = nums2[q]
                q += 1
            

        
        while p<m:
            temp[i] = nums1[p]
            p += 1
            i += 1

        while q<n:
            temp[i] = nums2[q]
            i += 1
            q += 1

        for i in range(s):
            nums1[i] = temp[i]

       


       
        
        