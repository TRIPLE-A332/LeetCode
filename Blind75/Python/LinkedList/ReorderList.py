class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        nodes = []

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        list1 = ListNode(0)
        tail = list1

        l , r = 0 , len(nodes)-1
        count = 0
        while l <= r :
            if count%2 == 0:
                tail.next = nodes[l]
                tail = tail.next
                l+=1
            else:
                tail.next = nodes[r]
                tail = tail.next
                r-=1
            count+=1
        
        tail.next = None