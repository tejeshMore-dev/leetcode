/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {number} a
 * @param {number} b
 * @param {ListNode} list2
 * @return {ListNode}
 */

var mergeInBetween = function(list1, a, b, list2) {
    let counter = 0;
    let list2Tail = null
    
    let node = list2;
    while (1) {
        if (node.next)
            list2Tail = node.next;    
        else 
            break
        
        node = node.next
    }
    
    node = list1;
    while(node) {
        if(counter === b)  {
            list2Tail.next=node.next;
            node.next = null
            break
        }
                
        counter++;
        node = node.next;
    }
    
    counter = 1;
    node = list1;
    while(node) {
        if(counter === a)  {
            node.next=list2;
            break
        }
                
        counter++;
        node = node.next;
    }
      
    return list1;
};