# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return []
        ans = []

        def travel(root):

            if not root: return


            ans.append(root.val)
            if root.left:
                travel(root.left)
            if root.right:
                travel(root.right)

        
        travel(root)
        return ans