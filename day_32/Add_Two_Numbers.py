# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = carry + x + y
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummy.next
