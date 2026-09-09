/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let node = new ListNode();
    let start = node;

    while( list1 || list2 ) {
        if( !list1 ) {
            node.next = list2;
            break;
        }

        if( !list2 ) {
            node.next = list1;
            break;
        }
        
        if( list1.val <= list2.val ) {
            let nextNode = list1.next;
            node.next = list1;
            node = list1;
            list1 = nextNode;
        } else {
            let nextNode = list2.next;
            node.next = list2;
            node = list2;
            list2 = nextNode;
        }
    }

    return start.next;
};