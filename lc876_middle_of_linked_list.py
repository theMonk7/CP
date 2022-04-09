class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = f = head
        while f and f.next is not None:
            s = s.next
            f = f.next.next
        return s