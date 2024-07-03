# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        seen=set()
        todel=set()
        while cur:
            if cur.val not in seen:
                seen.add(cur.val)
            else:
                todel.add(cur.val)
            cur=cur.next
        dummy=ListNode(0,head)
        prev=dummy
        cur=head
        while cur is not None:
            if cur.val in todel:
                prev.next,cur.next=cur.next,None
                cur=prev.next
            else:
                prev=cur
                cur=cur.next
        return dummy.next
        
