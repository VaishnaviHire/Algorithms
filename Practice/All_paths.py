# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        res_list = []
        if not root:
            return res_list

        stack = [(root,0)]
        path = []

        while stack:
            vertex, height = stack.pop()
            path.append(str(vertex.val))

            if vertex.right:
                stack.append((vertex.right,height+1))
            if vertex.left:
                stack.append((vertex.left,height+1))

            if not vertex.left and not vertex.right:
                res_list.append('->'.join(path))
                if stack:
                    parent_h = stack[-1][1]
                    while len(path) > parent_h:
                        path.pop()

        return res_list






a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)

a1.left = a2
a1.right = a3
a2.left = a4

b = Solution()

print b.binaryTreePaths(a1)
