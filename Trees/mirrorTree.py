#attribution: www.leetcode.com
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSymm(Left, Right):
            if not Left and not Right:
                return True
            if Left and Right and Left.val == Right.val:
                return isSymm(Left.left, Right.right) and isSymm(Left.right, Right.left)
            return False
        
        return isSymm(root, root)