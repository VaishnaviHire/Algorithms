# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        self.diameterOfBinaryTree1(root)
        return self.ans - 1

    def diameterOfBinaryTree1(self, root) -> int:
        if not root:
            return 0

        r = self.diameterOfBinaryTree1(root.right)
        l = self.diameterOfBinaryTree1(root.left)

        self.ans = max(self.ans, l + r + 1)

        return max(l, r) + 1



