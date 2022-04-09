class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fPtr = sPtr = head
        while fPtr and fPtr.next != None:
            fPtr = fPtr.next.next
            sPtr = sPtr.next
            if fPtr == sPtr:
                return True

        return False