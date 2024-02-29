# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallnode = ListNode()
        head1 = smallnode
        largenode= ListNode()
        head2= largenode
        newnode= ListNode()
        head3= newnode
        while head is not None:
            if head.val < x:
                head1.next = ListNode(head.val)
                head1=head1.next
            elif head.val >=x:
                head2.next = ListNode(head.val)
                head2= head2.next
            head = head.next
            
        smallnode= smallnode.next
        largenode= largenode.next
        while smallnode is not None and largenode is not None:
            if smallnode.val < largenode.val:
                head3.next = smallnode
                smallnode = smallnode.next
            else:
                head3.next = largenode
                largenode = largenode.next
            head3 = head3.next

        if smallnode is not None:
            head3.next = smallnode
        elif largenode is not None:
            head3.next = largenode
        return newnode.next