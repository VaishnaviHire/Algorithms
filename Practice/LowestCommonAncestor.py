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

        def dfs(root, par=None):
            if root:
                root.par = par
                dfs(root.left, root)
                dfs(root.right, root)

        dfs(root)

        p_list =[]
        q_list = []

        def dfs_par(root, lis):
            if root:
                if root.par:
                    lis.append(root.par.val)
                dfs(root.par)

        dfs_par(p,p_list)
        dfs_par(q,q_list)
        a = min([value for value in p_list if value in q_list])
        if a:
            return a
        else:
            return root


