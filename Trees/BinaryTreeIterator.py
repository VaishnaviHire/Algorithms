# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.curr = root

    def findInorderSuccessor(self,root,p):
        stack = []
        flag = 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if flag == 1:
                return stack.pop()

            root = stack.pop()
            if root == p:
                flag = 1
            root = root.right
        return None

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.findInorderSuccessor(self.root, self.curr):
            return True
        return False


    def next(self):
        """
        :rtype: int
        """
        self.curr = self.findInorderSuccessor(self.root, self.curr)
        return  self.curr.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())