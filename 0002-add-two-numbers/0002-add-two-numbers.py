# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        DummyHead = ListNode(0)
        carry = 0
        curr = DummyHead
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            
            newVal = (l1Val + l2Val + carry) % 10
            carry = (l1Val + l2Val + carry) // 10
            newNode = ListNode(newVal)

            curr.next = newNode
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return DummyHead.next


        