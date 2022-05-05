# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None and list2 is None:
            return None
        elif list1 is None and list2:
            return list2
        elif list2 is None and list1:
            return list1

        temp = list1
        merged = self.mergeTwoLists(list1.next, list2)
        if merged.val >= temp.val:
            temp.next = merged
            return temp
        else:
            t = merged
            while t.next:
                if t.next.val < temp.val:
                    t = t.next
                else:
                    temp.next = t.next
                    t.next = temp
                    return merged
            t.next = temp
            return merged

