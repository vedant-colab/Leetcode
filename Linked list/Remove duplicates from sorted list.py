class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next

            else:
                curr = curr.next

        return head