# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            time complexity : O(n)
            space complexity : O(1)
        """
        if head is None:
            return None
        slow = head
        fast = head
        while fast is not None:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
            slow.next = None
        return head
        

        