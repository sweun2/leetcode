# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = []
        cnt = 0
        cur = head
        while cur:
            result.append(cur)
            cur = cur.next


        ri = len(result) - n

        if ri -1 >=0 and ri + 1 < len(result): # 중간
            result[ri-1].next = result[ri+1]
        elif ri -1 >=0 and ri + 1 >= len(result):  # 마지막
            result[ri-1].next = None
        elif ri-1 <0 and ri + 1 < len(result): #처음
            head = head.next
        else:
            head = None
        
        return head


