# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        current = head
        currentIndex = 1
        removeWhere =  self.getLenOfLinkedList(head) - n
        while currentIndex < removeWhere-1:
            currentIndex = currentIndex + 1
            current = current.next
        current.next = current.next.next

    def getLenOfLinkedList(self,head):
        len = 0
        current = head
        if head == None:
            return 0
        else:
            while current.next == True:
                len = len + 1
                current = current.next
            len = len + 1
            return len
