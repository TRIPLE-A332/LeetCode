package Blind75.LinkedList;


public class ReverseList {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while(curr!=null)
        {   
            ListNode temp = curr.next;
            curr.next = prev;
            prev=curr;
            curr=temp;
        }
        return head;
    }
    public static void main(String[] args) {
        
    }
}
