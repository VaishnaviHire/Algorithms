class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left_height = 0
        right_height = 0

        def findHeight(root, left_height, right_height):
            if root.left:
                left_height += findHeight(root.left, left_height + 1, right_height)[0]
            if root.right:
                right_height += findHeight(root.right, left_height, right_height + 1)[1]
            return (left_height, right_height)

        print findHeight(root, left_height, right_height)


a = Solution()
a1 = TreeNode(3)
a2 = TreeNode(9)
a3 = TreeNode(20)
a4 = TreeNode(15)
a5 = TreeNode(7)
a1.left = a2
a1.right = a3
a3.left = a4
a3.right = a5
a.isBalanced(a1)
