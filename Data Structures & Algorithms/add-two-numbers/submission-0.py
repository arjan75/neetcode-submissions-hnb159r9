# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def traverse(l1):
            strValue = ""
            while l1:
                strValue += str(l1.val)
                l1 = l1.next
            return int(strValue[::-1])

        l1Value = traverse(l1)
        l2Value = traverse(l2)

        total = str(l1Value + l2Value)
        reverseTotal = total[::-1] 
        

        head = ListNode(val=int(reverseTotal[0]))
        temp = head
        for i in range(1, len(reverseTotal)):
            temp.next = ListNode(val=int(reverseTotal[i]))
            temp = temp.next
        return head






        