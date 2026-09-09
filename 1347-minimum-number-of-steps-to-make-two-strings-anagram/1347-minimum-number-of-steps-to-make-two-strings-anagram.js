/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var minSteps = function(s, t) {
    let charCountObject = {};
    let result = 0;
    
    for (char of s) {
        charCountObject[char] = charCountObject[char] ? charCountObject[char]+1 : 1;  
    }
     
        
     for (char of t) {
         if (charCountObject[char])
             charCountObject[char] = charCountObject[char]-1;
    }
        
    for (char in charCountObject) {
        if(charCountObject[char] > 0 )
            result += charCountObject[char];
    } 
    
    return result
};