class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        cur = head

        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur

            cur = cur.next

        return dummy.next
        
        