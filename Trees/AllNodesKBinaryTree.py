# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        def dfs(root,par=None):
            if root:
                root.par = par
                dfs(root.left,root)
                dfs(root.right,root)
        dfs(root)
        #bfs with dist

        queue = [(target,0)]
        visited = []
        result = []
        while queue:
            if queue[0][1] == K:
                break

            curr,dist = queue.pop(0)
            if curr.left and curr.left not in visited:
                queue.append((curr.left,dist+1))
                visited.append(curr.left)
            if curr.right and curr.right not in visited:
                queue.append((curr.right,dist+1))
                visited.append(curr.right)
            if curr.par and curr.par not in visited:
                queue.append((curr.par,dist+1))
                visited.append(curr.par)

        if queue:
            for i in queue:
                result.append(i[0].val)
        if target.val not in result:
            result = []
        else:
            result.remove(target.val)
        return result

a = Solution()
a3 = TreeNode(3)
a5 = TreeNode(5)
a1 = TreeNode(1)
a6 = TreeNode(6)
a2 = TreeNode(2)
a0 = TreeNode(0)
a8 = TreeNode(8)
a7 = TreeNode(7)
a4 = TreeNode(4)

a3.left = a5
a3.right = a1
a1.left = a0
a1.right=a8
a5.left = a6
a5.right = a2
a2.left = a7
a2.right=a4

print a.distanceK(a3,a5,2)