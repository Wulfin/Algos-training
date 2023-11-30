class ListNode2 {
     int val;
      ListNode2 next;
      ListNode2() {}
      ListNode2(int val) { this.val = val; }
      ListNode2(int val, ListNode2 next) { this.val = val; this.next = next; }
  }
public class Remove_Duplicatesfrom_Sorted_List_II {
    public ListNode2 deleteDuplicates(ListNode2 head) {
        ListNode2 node = head;
        boolean firstValNotEqual = false;
        //ListNode2 node2 = head.next;

        while (node.next != null){
            if (node.next.val == node.val || firstValNotEqual){
                firstValNotEqual = true;
                node.next = node.next.next;
                node.val= node.next.val;
                if (node.next.val != node.val){
                    firstValNotEqual = false;
                }
            }
        }

        return head;
    }
}
