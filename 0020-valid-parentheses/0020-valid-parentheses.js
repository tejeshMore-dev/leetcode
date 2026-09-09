/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    if( s.length === 1 )
        return false
    
    if( s.length === 0 )
        return true

    let openingBrackts =  new Set(["{", "(", "[" ]);
    let c2oMapping = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    let stack = [];

    for( let char of s ) {
        if( openingBrackts.has(char) )
            stack.push(char);
        else {
            if(  stack[stack.length-1] !== c2oMapping[char] )
                return false
            else
                stack.pop();
        }
    }

    return stack.length === 0;
};

/*

if opening
stack push

if closing 
stack top = oppp if current
stack pop

stack empty

*/