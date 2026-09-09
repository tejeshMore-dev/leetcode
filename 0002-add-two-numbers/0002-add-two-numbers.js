/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let c = 0;
    let head = new ListNode();
    let current = head;

    while(l1 || l2 || c) {
        let sum = 0;
        if( l1 )
            sum += l1.val;

        if( l2 )
            sum += l2.val;
            
        if( c )
            sum += c;


        if( sum > 9 ){
            let remainder = sum - 10;
            c = 1;
            let newNode =  new ListNode(remainder);
            current.next = newNode;
            current = newNode            
        } else {
            c = 0;
            let newNode =  new ListNode(sum);
            current.next = newNode;
            current = newNode
        }

        l1 = l1 ? l1.next : l1;
        l2 = l2 ? l2.next : l2;
    }

    return head.next;
};