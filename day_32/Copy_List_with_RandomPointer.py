class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_dict = {}
        head_copy = Node(head.val)
        node_dict[head] = head_copy
        
        curr = head
        curr_copy = head_copy
        
        while curr.next:
            curr = curr.next
            if curr not in node_dict:
                node = Node(curr.val)
                node_dict[curr] = node
            curr_copy.next = node_dict[curr]
            curr_copy = curr_copy.next
        
        curr = head
        curr_copy = head_copy
        lock = True     # Lock the loop to run only once more
        
        while curr.next or lock:
            if curr.random:
                node_dict[curr_copy].random = node_dict[curr.random]
                curr_copy.random = node_dict[curr_copy].random
            
            if not curr.next: break
            curr = curr.next
            curr_copy = curr_copy.next
        
        return head_copy
    
    
def main():
    # Create the original linked list
    nodes_data = [
        [7,None],[13,0],[11,4],[10,2],[1,0]
    ]
    
    # Create the nodes with values and random pointers
    nodes = []
    for data in nodes_data:
        node = Node(data[0])
        nodes.append(node)
    
    for i, data in enumerate(nodes_data):
        if data[1] is not None:
            nodes[i].random = nodes[data[1]]
    
    # Connect the nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Copy the linked list
    copied_list = solution.copyRandomList(nodes[0])
    
    # Print the values and random pointers of the copied list
    curr = copied_list
    while curr:
        print("Value:", curr.val)
        if curr.random:
            print("Random Pointer:", curr.random.val)
        else:
            print("Random Pointer: None")
        print()
        curr = curr.next

# Call the main function
main()
