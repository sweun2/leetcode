# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dup = set()
        cur = head
        
        temp = cur
        while cur:
            if cur.val not in dup:
                dup.add(cur.val)
                temp = cur
                cur = cur.next
            else:
                while cur != None and cur.val in dup:
                    cur= cur.next
                temp.next = cur
        return head

            

            