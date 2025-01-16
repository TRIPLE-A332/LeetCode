package Blind75.LinkedList;
import java.util.*;

public class ReverseList {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        LinkedList<Integer> ll = new LinkedList<>();

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
