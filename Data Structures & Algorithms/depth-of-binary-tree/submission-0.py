# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        if not root: return 0

        ans = 0
        st = [(root,1)]

        while st:

            node,level = st.pop()
            ans = max(ans,level)

            if node.left:
                st.append((node.left,level+1))
            if node.right:
                st.append((node.right,level+1))

        return ans

            




