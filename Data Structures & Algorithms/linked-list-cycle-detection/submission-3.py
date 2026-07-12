# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = []
        curr = head
        while curr:
            if curr not in index:
                index.append(curr)
                curr = curr.next
            else:
                return True
        return False
        