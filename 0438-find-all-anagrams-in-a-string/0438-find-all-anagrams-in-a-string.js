/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    let result = [];
    let stringLength = p.length;
    let lp = 0;
    let  charCountObj = {};
    
    for (let char of p) {
         charCountObj[char] =  charCountObj[char] ? charCountObj[char]+1 : 1
    }
    
     while (lp < s.length) {
         let str = s.slice(lp, lp+stringLength);
         
         if (stringLength - str.length !== 0) {
            return result;
         }
         
         if (isAnagrams(str, charCountObj))
             result.push(lp);
        lp++
     }
    
    return result;
    
};

function isAnagrams(str, charCountObj) {
    let charCountObjCopy = JSON.parse(JSON.stringify(charCountObj));
    for (let char of str) {
         if ( charCountObjCopy[char] && charCountObjCopy[char] > 0)
             charCountObjCopy[char] = charCountObjCopy[char]-1;
        else  {
            return false
            
        }
    }
    return true;
}