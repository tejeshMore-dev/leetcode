/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    let result = [];
    
    traverse(root);
    return result.join(",");
    
    function traverse(root) {
        if( !root ) {
            result.push('null');
            return        
        }
        
        result.push(root.val);
        traverse(root.left);
        traverse(root.right);
    }
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    let inp = data.split(",");
    let i = 0;
    return traverse();
    
    function traverse() {
        let val = inp[i++];
        if( val === "null" ) {
            return null;
        }
        
        let node = new TreeNode( parseInt(val) );
        node.left = traverse()
        node.right = traverse()   
        return node;
    }
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */