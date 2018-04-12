#attribution - www.leetcode.com
# Given a linked list, remove the nth node from the end of list and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = head
        p2 = head     
      
        for i in range(n):
            p1 = p1.next
                    
        if not p1:
            return head.next
            
        else:
        
            while p1.next:
                p1 = p1.next
                p2 = p2.next           
            
            p2.next = p2.next.next

            return head