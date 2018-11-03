# Convert
# a
# BST
# to
# a
# sorted
# circular
# doubly - linked
# list in -place.Think
# of
# the
# left and right
# pointers as synonymous
# to
# the
# previous and next
# pointers in a
# doubly - linked
# list.
#
# Let
# 's take the following BST as an example, it may help you understand the problem better:
#
# We
# want
# to
# transform
# this
# BST
# into
# a
# circular
# doubly
# linked
# list.Each
# node in a
# doubly
# linked
# list
# has
# a
# predecessor and successor.For
# a
# circular
# doubly
# linked
# list, the
# predecessor
# of
# the
# first
# element is the
# last
# element, and the
# successor
# of
# the
# last
# element is the
# first
# element.
#
# The
# figure
# below
# shows
# the
# circular
# doubly
# linked
# list
# for the BST above.The "head" symbol means the node it points to is the smallest element of the linked list.
#
# Specifically, we
# want
# to
# do
# the
# transformation in place.After
# the
# transformation, the
# left
# pointer
# of
# the
# tree
# node
# should
# point
# to
# its
# predecessor, and the
# right
# pointer
# should
# point
# to
# its
# successor.We
# should
# return the
# pointer
# to
# the
# first
# element
# of
# the
# linked
# list.
#
# The
# figure
# below
# shows
# the
# transformed
# BST.The
# solid
# line
# indicates
# the
# successor
# relationship,
# while the dashed line means the predecessor relationship.




# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right



class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        if not root.left and not root.right:
            return root
        def inorder(temp):
            stack = []
            result = []
            while temp or stack:
                while temp:
                    stack.append(temp)
                    temp = temp.left
                temp = stack.pop()
                result.append(temp)
                temp = temp.right
            return result

        result = inorder(root)
        for i in range(1,len(result)-1):
            result[i].left = result[i-1]
            result[i].right = result[i+1]

        result[0].right = result[1]
        result[0].left = result[len(result)-1]
        result[len(result)-1].right = result[0]
        result[len(result)-1].left = result[len(result)-2]

        return result[0]
a = Solution()
a1 = Node(1,None,None)
a5 = Node(5,None,None)
a3 = Node(3,None,None)
a2 = Node(2,a1,a3)
a4 = Node(4,a2,a5)


a11 = (a.treeToDoublyList(a4))
while a11.val != 2:
    print(a11.val)
    a11 = a11.left


