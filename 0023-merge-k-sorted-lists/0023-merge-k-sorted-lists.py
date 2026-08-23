# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_lists(list1, list2):
            dummy = ListNode(None)
            current = dummy

            while list1 or list2:
                if list1 and not list2:
                    current.next = list1
                    break
                
                if not list1 and list2:
                    current.next = list2
                    break

                if list1.val <= list2.val:
                    current.next = list1
                    current = current.next
                    list1 = list1.next
                else:
                    current.next = list2
                    current = current.next
                    list2 = list2.next

            return dummy.next

        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = merge_lists(lists[i], lists[i+interval])
            
            interval *= 2
        
        return lists[0]


        