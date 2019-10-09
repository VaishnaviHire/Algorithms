# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s, t) -> bool:

        def traverse(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if isEqual(t1, t2):
                return True
            return traverse(t1.left, t2) or traverse(t1.right, t2)

        def isEqual(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False

            return (t1.val == t2.val) and isEqual(t1.right, t2.right) and isEqual(t1.left, t2.left)

        return traverse(s, t)