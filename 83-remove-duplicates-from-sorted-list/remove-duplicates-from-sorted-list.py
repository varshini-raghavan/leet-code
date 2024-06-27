# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev=head
        cur=head.next
        while cur is not None:
            print(prev.val,cur.val)
            if prev.val==cur.val:
                prev.next=cur.next
                cur=cur.next
            else:
                prev=prev.next
                cur=cur.next
        return head