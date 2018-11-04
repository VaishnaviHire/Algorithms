# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def depth(self,root):
        if root:
            return max(self.depth(root.left), self.depth(root.right)) + 1
        return 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right), (self.depth(root.left) + self.depth(root.right)))
        return 0






a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)

a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5


# a2.left = a1
# a1.left = a3
# a2.right = a4
# a4.left = a5

b = Solution()
print b.diameterOfBinaryTree(a1)

