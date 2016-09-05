class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val,repr(self.next))

class Solution:
    def reverseList(self,head):
        reverse = ListNode(float("-inf"))
        while head:
            reverse.next, head.next, head = head, reverse.next, head.next
        return reverse.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution().reverseList(head)
