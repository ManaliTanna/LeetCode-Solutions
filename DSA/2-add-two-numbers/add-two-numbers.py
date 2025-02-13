# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = ListNode()
        current = answer
        carry = 0
        while (carry != 0 or l1 != None or l2 != None):
            
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0

            total = l1_value + l2_value + carry

            carry = total // 10

            current.next = ListNode(total % 10)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return answer.next



        