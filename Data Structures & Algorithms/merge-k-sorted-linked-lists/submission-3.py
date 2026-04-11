# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(l1, l2):
            dummy = ListNode(0)
            tail = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            # attach remaining
            tail.next = l1 if l1 else l2

            return dummy.next

        if not lists:
            return None

        res = lists[0]
        for i in range(1, len(lists)):
            res = merge(res, lists[i])

        return res