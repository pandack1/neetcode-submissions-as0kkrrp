# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = []
        self.ctr = 0
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            self.result.append(root.val)
            dfs(root.right)
        dfs(root)
        if self.result and k <= len(self.result):
            return self.result[k-1]
        else:
            return None
            
        