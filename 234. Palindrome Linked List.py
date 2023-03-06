class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode):
        fast = head
        slow = head

        while fast and fast.next:       #both need to have values. We don't want t jump to a null value b/c it would skew our middle.
            fast = fast.next.next
            slow = slow.next            #the slow pointer will become the middle.

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        left, right = head , prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True