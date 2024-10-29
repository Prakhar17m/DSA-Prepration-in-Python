class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head

        while temp and temp.val == val:
            temp = temp.next
        
        ret = temp
        prev = temp

        while temp:
            if temp.val != val:
                if temp != prev:
                    prev.next = temp
                prev = temp
            temp = temp.next
        if prev:
            prev.next = None
        return ret
