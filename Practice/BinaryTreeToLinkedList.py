# Given a binary tree, flatten it to a linked list in-place.
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:


    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        li = []

        def inorder( root, li):
            if root:
                li.append(root)
                inorder(root.left, li)
                inorder(root.right, li)
            return "None"

        inorder(root,li)

        if li:
            head = li[0]
            head.left = None
            prev = head
        for node in li[1:]:
            prev.right = node
            node.left = None
            prev = node






a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a6 = TreeNode(6)

a1.left = a2
a1.right = a5
a2.left = a3
a2.right = a4
a5.right = a6

b = Solution()
print b.flatten(a1)