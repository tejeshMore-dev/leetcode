
var MyLinkedList = function() {
    this.head = null;
};

class Node{
    constructor(value) {
        this.val = value;
        this.next = null;
    }
}

/** 
 * @param {number} index
 * @return {number}
 */
MyLinkedList.prototype.get = function(index) {
    let node = this.head;
    
    while(node) {
        if(index === 0)
            return node.val
            
        index--;
        node = node.next;
    }
    
    return -1;
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtHead = function(val) {
    let node = this.head;
    
    this.head = new Node(val);
    this.head.next = node;
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtTail = function(val) {
    let node = this.head;
    
    if(!node) {
        this.head = new Node(val);
        return;
    }
    
    while(node.next) {
        node = node.next;
    }
    
    node.next = new Node(val);
};

/** 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtIndex = function(index, val) {
    let node = this.head;
    
    if(index === 0){
        this.head = new Node(val);
        this.head.next = node;    
        return;
    }
    
    
    while(node) {
        if(index === 1) {
            let nextNode = node.next;
            let newNode = new Node(val);
            
            node.next = newNode;
            
            if(nextNode)
                newNode.next = nextNode;
            
            return;
        }
        
        index--;
        node = node.next
    }
};

/** 
 * @param {number} index
 * @return {void}
 */
MyLinkedList.prototype.deleteAtIndex = function(index) {
    if(index === 0) {
        this.head = this.head.next;
        return;
    }
        
        
    let node = this.head;
    
    while(node) {
        if(index === 1) {
            let targetNode = null;
            let nextNode = null;
            let prevNode = node;
            
            if(prevNode.next)
                targetNode = prevNode.next
            
            if(targetNode && targetNode.next)
                nextNode = targetNode.next
            
            prevNode.next = nextNode
            return;
        }
        
        index--;
        node = node.next;
    }
    
};

/** 
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = new MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */