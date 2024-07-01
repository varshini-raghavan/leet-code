# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        lst=[]
        while cur is not None:
            lst.append(cur.val)
            cur=cur.next
        lst.sort()
        cur=head
        for i in lst:
            cur.val=i
            cur=cur.next
        return head