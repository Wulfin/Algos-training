class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        headNext = head.next
        if headNext.next == None:
            headNext.next = head
            head.next = None
            return headNext
        
        curr = head
        currNext = head.next
        currNextNext = head.next.next
        head = head.next
        pointerSaved = None
        
        while True:
            pointerSaved = currNextNext
            currNext.next = curr
            if not currNextNext.next:
                curr.next = currNextNext
                break
            curr.next = currNextNext.next
            
            curr = pointerSaved
            currNext = curr.next
            if not currNext.next:
                currNext.next = curr
                curr.next = None
                break
            currNextNext = curr.next.next
            
        return head


def createLinkedList(nums):
    if not nums:
        return None
    
    head = ListNode(nums[0])
    curr = head
    
    for i in range(1, len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next
    
    return head

def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()
    

if __name__ == "__main__":
    nums = [1,2,3,4]
    head = createLinkedList(nums)
    
    solution = Solution()
    swapped_head = solution.swapPairs(head)
    
    print("Swapped Linked List:")
    printLinkedList(swapped_head)