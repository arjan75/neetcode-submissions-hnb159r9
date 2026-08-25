# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        current = dummy

        while heap:
            value, index, node = heapq.heappop(heap)
            current.next = node
            current = node
            node = node.next

            if node:
                heapq.heappush(heap, (node.val, index, node))
        return dummy.next


        