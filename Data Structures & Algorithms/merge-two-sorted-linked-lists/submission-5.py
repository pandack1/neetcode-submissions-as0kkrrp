# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        if not l1:
            return l2
        elif not l2:
            return l1
        head = l1
        i=0
        prev = l1
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    if i != 0:
                        prev.next = l1
                        prev = l1
                        l1 = l1.next
                    elif i == 0:
                        head = l1
                        prev = l1
                        l1 = l1.next
                        i += 1
                else:
                    if i != 0:
                        prev.next = l2
                        prev = l2
                        l2 = l2.next
                    elif i == 0:
                        head = l2
                        prev = l2
                        l2 = l2.next
                        i += 1
            elif l1 and not l2:
                prev.next = l1
                break
            elif l2 and not l1:
                prev.next = l2
                break
        return head


        