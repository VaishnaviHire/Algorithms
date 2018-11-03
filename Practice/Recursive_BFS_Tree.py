class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recursive_bfs(self,root):
        if not root:
            return
        return








a = Solution()
a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a6 = TreeNode(6)

a1.left = a2
a1.right = a3
a3.right = a6
a2.left = a4
a2.right = a5

print a.recursive_bfs(a1)