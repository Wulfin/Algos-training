# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head: ListNode, n):
        N_nodes = [head]
        node: ListNode = head
        while node.next is not None:
            if len(N_nodes) >= n + 1:
                N_nodes = N_nodes[1:] + [node.next]
            else:
                N_nodes.append(node.next)
            node = node.next

        if len(N_nodes) <= n:
            return head.next
        N_nodes[0].next = N_nodes[1].next
        return head


if __name__ == "__main__":
    solution = Solution()

    Nodes = [ListNode(0)]
    for i in range(1, 56):
        Nodes.append(ListNode(i))
        Nodes[i - 1].next = Nodes[i]

    node = Nodes[0]
    for i in range(1, 56):
        print(node, " val =", node.val)
        node = node.next

    res = solution.removeNthFromEnd(Nodes[0], 2)

    print("\n\n########################\n\n")
    node = Nodes[0]
    for i in range(1, 56):
        print(node, " val =", node.val)
        node = node.next
