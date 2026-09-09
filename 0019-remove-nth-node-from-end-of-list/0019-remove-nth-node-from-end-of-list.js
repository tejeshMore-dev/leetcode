/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let dummyNode = new ListNode(-1);
    dummyNode.next = head;
    
    let length=0;
    let currentNode = head;
    while( currentNode ) {
        length++;
        currentNode = currentNode.next;
    }
    
    let mid = length-n;
    currentNode = dummyNode;
    while( mid ) {
        currentNode = currentNode.next;
        mid--;
    }
    
    currentNode.next = currentNode.next ? currentNode.next.next : null;
    
    return dummyNode.next;
};
/*
[1,2,3,4,5]

dummy.next = head;
current = dummy;

2-2

0
*/