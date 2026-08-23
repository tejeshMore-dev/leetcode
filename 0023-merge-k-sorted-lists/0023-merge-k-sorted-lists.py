# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        merged_list = lists[0]
        n = len(lists)

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

        for i in range(1, n):
            list2 = lists[i]
            merged_list = merge_lists(merged_list, list2)
        
        return merged_list


        