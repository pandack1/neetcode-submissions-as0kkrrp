# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = None
        self.ctr = 0
        def dfs(root):
            if not root or self.result:
                return None
            dfs(root.left)
            self.ctr += 1
            if self.ctr == k:
                self.result = root.val
                return
            dfs(root.right)
        dfs(root)
        return self.result
        