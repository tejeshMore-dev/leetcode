/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let lp = 0, rp = s.length-1;
    while( s[rp] === " " ){
        rp--;
    }
    
    let end = rp;
    while( s[rp] !== " " && rp >= 0 ) {
        rp--
    }
    
    return end-rp;
};