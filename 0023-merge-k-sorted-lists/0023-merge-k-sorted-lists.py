# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        min_heap = []

        for i, _ in enumerate(lists):
            node = lists[i]
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        dummy = ListNode()
        tail = dummy

        while min_heap:
            val, i,  node = heapq.heappop(min_heap)
            tail.next = ListNode(val)
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
            
            tail = tail.next

        return dummy.next


        