# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        cur=head
        length=1
        while cur.next:
            cur=cur.next
            length+=1
        cur.next=head
        k=k%length
        k=length-k
        prev=None
        cur=head
        while k:
            prev=cur
            cur=cur.next
            k-=1
        prev.next=None
        return cur

        