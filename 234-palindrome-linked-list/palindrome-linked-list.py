# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        palin=[]
        cur=head
        while cur is not None:
            palin.append(cur.val)
            cur=cur.next
        i=0
        j=len(palin)-1
        while i<j:
            if palin[i]!=palin[j]:
                return False
            i+=1
            j-=1
        return True

            
