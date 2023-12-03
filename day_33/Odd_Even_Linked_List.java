class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}


class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null) return null;

        if (head.next == null || head.next.next == null) return head;

        
        ListNode lastOdd = head;
        ListNode lastEven = head.next;
        ListNode firstEven = head.next;
        ListNode curr = head.next.next;
        int index = 3;

        while (curr != null) {
            if (index%2 == 1) {
                lastOdd.next = curr;
                lastOdd = curr;
            }
            else {
                lastEven.next = curr;
                lastEven = curr;
            }

            curr = curr.next;
            index++;
        }

        lastOdd.next = firstEven;
        lastEven.next = null;
            
        return head;
    }
}


public class Odd_Even_Linked_List {
    public static void main(String[] args) {
        // Create an array of integers
        int[] arr = {1, 2, 3, 4, 5};

        // Create a linked list from the array
        ListNode head = createLinkedList(arr);

        // Create an instance of the Solution class
        Solution solution = new Solution();

        // Call the oddEvenList method and print the result
        ListNode result = solution.oddEvenList(head);
        printLinkedList(result);
    }

    // Helper method to create a linked list from an array
    private static ListNode createLinkedList(int[] arr) {
        ListNode dummy = new ListNode();
        ListNode curr = dummy;

        for (int num : arr) {
            curr.next = new ListNode(num);
            curr = curr.next;
        }

        return dummy.next;
    }

    // Helper method to print a linked list
    private static void printLinkedList(ListNode head) {
        ListNode curr = head;

        while (curr != null) {
            System.out.print(curr.val + " ");
            curr = curr.next;
        }

        System.out.println();
    }
}
