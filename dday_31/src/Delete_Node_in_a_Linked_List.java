// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
public class Delete_Node_in_a_Linked_List {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
    public static void main(String[] args) {

    }
}