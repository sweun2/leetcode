# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        visited = []
        while cur:
            visited.append(cur.val)
            cur = cur.next
        
        left = 0
        right = len(visited) - 1

        while left < right:
            if visited[left] != visited[right]:
                return False
            else:
                left +=1
                right -=1
        
        return True



