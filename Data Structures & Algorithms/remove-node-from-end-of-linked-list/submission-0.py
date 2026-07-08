# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next
        curr = head

        if length == n:
            curr = curr.next
            return curr
        
        count = 0

        while curr:
            if count == length - n - 1:
                curr.next = curr.next.next
                return head
            else:
                curr = curr.next
                count += 1
            
        