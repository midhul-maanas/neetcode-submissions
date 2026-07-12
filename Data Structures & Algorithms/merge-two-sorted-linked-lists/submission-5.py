# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        # curr = list1
        # head1 = list1
        # head2 = list2
        # while curr != None:
        #     nxt1 = curr.next
        #     curr.next = list2
        #     nxt2 = list2.next if list2.next != None else list1.next
        #     list2.next = nxt1
        #     list2 = nxt2
        #     curr = nxt1
        # curr = head1
        # while not curr:
        #     nxt1.next = curr
        # curr = head2
        # while not curr:
        #     nxt1.next = curr
        # curr = head1


        # #sort
        # while curr.next != None:
        #     if curr.next.val < curr.val:
        #         temp = curr.val
        #         curr.val = curr.next.val
        #         curr.next.val = temp
        #     curr = curr.next

        #method2
        # curr1 = list1 if list1.val < list2.val else list2
        # curr2 = list2 if list1.val < list2.val else list1

        # while curr1.next:
        #     if curr1.next.val < curr2.val:
        #         nxt = curr1.next
        #     else:
        #         nxt = curr2.next
        #     curr1.next = nxt
        #     curr1 = nxt


        dummy=res = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next
        res.next = list1 or list2
    


        return dummy.next
        