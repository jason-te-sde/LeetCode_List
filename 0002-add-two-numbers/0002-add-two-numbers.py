# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        value :[0 - 9]
        leading zero: 059
        len of linked list:[1, 100]
        TC: O(max(m, n))
        SC: O(1)
        """
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        # 1. Iterate until both lists are exhausted and no carry remains.
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            # 2. Calculate the current sum and update the carry for the next position.
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            # 3. Create a new digit node and advance all pointers.
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next

        