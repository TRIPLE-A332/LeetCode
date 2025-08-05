class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        curr = dummy
        right = head
        
        while n>0:
            right = right.next
            n-=1

        while right:
            right = right.next
            curr = curr.next
        
        curr.next = curr.next.next

        return dummy.next