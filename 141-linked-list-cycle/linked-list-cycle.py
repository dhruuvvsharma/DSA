class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head 

        while (fast != None and fast.next != None) : 
            slow = slow.next #x1
            fast = fast.next.next # x2

            if slow == fast:
                return True
        
        return False
