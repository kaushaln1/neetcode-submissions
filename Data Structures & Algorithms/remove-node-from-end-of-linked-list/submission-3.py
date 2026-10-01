# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fs, sl = head, head
        for _ in range(n):
            fs= fs.next
        
        if fs == None:
            return head.next

        while (fs.next):
            sl= sl.next
            fs= fs.next
        
         
        sl.next = sl.next.next

        return head

        