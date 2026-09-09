/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    //base condition
    if( s.length < 2)
        return true
    
    let result = true;
    let lp=0, rp=s.length-1;

    while( lp < rp ) {
        if( !isAlphanumeric(s[lp]) )
            lp++;
        else if( !isAlphanumeric(s[rp]) )
            rp--;
        else if( s[lp].toLowerCase() !== s[rp].toLowerCase() ) {
            result = false;
            break
        } else {
            lp++;
            rp--;
        }
    }

    return result

    function isAlphanumeric (str) {
          return /^[a-zA-Z0-9]+$/.test(str);
    }
};