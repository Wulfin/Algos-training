import java.util.LinkedList;
import java.util.List;

public class Reverse_Linked_List_II {
    public static void main(String[] args) {

        // Create a linked list from an array of values
        int[] values = {3,5};

        ListNode dummy = new ListNode();
        ListNode curr = dummy;

        for (int val : values) {
            curr.next = new ListNode(val);
            curr = curr.next;
        }

        ListNode head = dummy.next;

        // Test the reverseBetween method
        Solution solution = new Solution();
        int left = 1;
        int right = 2;
        ListNode reversed = solution.reverseBetween(head, left, right);

        // Print the reversed linked list
        while (reversed != null) {
            System.out.println(reversed.val + " ");
            reversed = reversed.next;
        }
    }
}

class ListNode {
    int val;
    ListNode next;

    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head.next == null || left == right) {
            return head;
        }

        ListNode curr = head;
        List<ListNode> nodesToReverseList = new LinkedList<>();
        ListNode nodeJustBeforeLeft = null;
        ListNode nodeJustAfterRight = null;
        int index = 0;

        while (curr != null) {
            if (index == left-2) {
                nodeJustBeforeLeft = curr;
            }

            if (index == right-1) {
                nodeJustAfterRight = curr.next;
                nodesToReverseList.addFirst(curr);
                break;
            }

            if (left-1 <= index && index <= right-1) nodesToReverseList.addFirst(curr);
            curr = curr.next;
            index++;
        }

        int size = nodesToReverseList.size();
        if (left != 1) nodeJustBeforeLeft.next = nodesToReverseList.get(0);
        nodesToReverseList.get(size-1).next = nodeJustAfterRight;

        for (int i = 0; i < size-1; i++){
            nodesToReverseList.get(i).next = nodesToReverseList.get(i+1);
        }
        
        if (left == 1) head = nodesToReverseList.get(0);
        return head;
    }
}


