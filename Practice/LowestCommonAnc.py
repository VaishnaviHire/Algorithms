# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        self.p_node= None
        self.q_node =None
        def dfs(root, par=None):
            if root:
                if root.val == p:
                    self.p_node = root
                elif root.val == q:
                    self.q_node = root
                root.par = par
                dfs(root.left, root)
                dfs(root.right, root)

        dfs(root)
        left_tree = []
        right_tree = []

        def dfs_par(root, lis):
            if root:
                if root.par:
                    lis.append(root.par.val)
                    dfs(root.par)

        if root.val == p or root.val == q:
            return root.val
        print self.p_node.val

        dfs_par(self.p_node, left_tree)
        dfs_par(self.q_node, right_tree)


        return min([value for value in left_tree if value in right_tree])

a =Solution()
a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a1.left=a2
a1.right =a3
a2.right =a4
print a.lowestCommonAncestor(a1, 4,2)