import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class Add_Two_Numbers_II {
    public static void main(String[] args) {
        BigInteger[] arr1 = {BigInteger.valueOf(3), BigInteger.valueOf(9), BigInteger.valueOf(9), BigInteger.valueOf(9), BigInteger.valueOf(9), BigInteger.valueOf(9), BigInteger.valueOf(9), BigInteger.valueOf(9), BigInteger.valueOf(9), BigInteger.valueOf(9)};
        BigInteger[] arr2 = {BigInteger.valueOf(7)};

        ListNode l1 = arrayToLinkedList(arr1);
        ListNode l2 = arrayToLinkedList(arr2);

        ListNode result = new Solution().addTwoNumbers(l1, l2);

        List<Integer> values = getAllValues(result);
        System.out.println(values);
    }

    private static ListNode arrayToLinkedList(BigInteger[] arr) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        for (BigInteger num : arr) {
            curr.next = new ListNode(num.intValue());
            curr = curr.next;
        }

        return dummy.next;
    }

    private static List<Integer> getAllValues(ListNode head) {
        List<Integer> values = new ArrayList<>();
        ListNode curr = head;

        while (curr != null) {
            values.add(curr.val);
            curr = curr.next;
        }

        return values;
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode resultHeadNode = new ListNode(0);
        BigInteger num1 = BigInteger.valueOf(l1.val);
        BigInteger num2 = BigInteger.valueOf(l2.val);

        ListNode node1 = l1;
        ListNode node2 = l2;

        while (node1.next != null) {
            num1 = num1.multiply(BigInteger.TEN).add(BigInteger.valueOf(node1.next.val));
            node1 = node1.next;
        }

        while (node2.next != null) {
            num2 = num2.multiply(BigInteger.TEN).add(BigInteger.valueOf(node2.next.val));
            node2 = node2.next;
        }

        BigInteger sum = num1.add(num2);
        String sumString = sum.toString();
        ListNode Node = resultHeadNode;

        for (int i = 0; i < sumString.length(); i++) {
            char charNumber = sumString.charAt(i);
            Node.val = Character.getNumericValue(charNumber);
            if (i == sumString.length()-1) {
                break;
            }
            Node.next = new ListNode();
            Node = Node.next;
        }

        return resultHeadNode;
    }
}