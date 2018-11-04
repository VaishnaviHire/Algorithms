#
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:

# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# Credits:
# Special thanks to @stellari for adding this problem and creating all test cases.

# Definition for singly-linked list.
import math
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def intersection(self,headA,headB):
        if headA == headB:
            return  headA
        else:
            while headA:
                headA = headA.next
                headB = headB.next
                if headA == headB:
                    return headA

        return None

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if headA and headB:
            la =0
            lb = 0
            temp_a = headA
            temp_b = headB
            while temp_a:

                temp_a = temp_a.next
                la +=1

            while temp_b:
                temp_b = temp_b.next
                lb +=1
            print la,lb

            diff = abs(lb-la)
            if la >= lb:
                for i in range(diff):
                    headA = headA.next

                return  self.intersection(headA,headB)

            else:
                print diff
                print headB.val

                for i in range(diff):
                    headB = headB.next

                print headB.val

                return  self.intersection(headB,headA)

        return None






a0 = ListNode(0)
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
b1 = ListNode(5)
b2 = ListNode(6)
a0.next = a1
a1.next = a2
a2.next = a3
a3.next = a4
b1.next = b2
b2.next = a3

c1 = ListNode(1)
d1 = ListNode(2)
d1.next = c1

li = Solution()
print li.getIntersectionNode(c1,d1).val