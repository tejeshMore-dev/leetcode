/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let resLength = 0;
    let res_l = 0;
    let res_r = 0;
    
    for (let index = 0; index<s.length; index++) { // O (n)
        // for odd case O(n)
        let i = index;
        let j = index;
        findMax(i,j,s);


        // for even case O(n)
        i = index;
        j = index+1;
        findMax(i,j,s);

    }
    return s.slice(res_l, res_r+1);  // O(n) * O(n + n) => O(n*n)
    
    function findMax(i,j) {
        while( i>=0 && i<s.length && s[i] === s[j] ) {
            if( resLength < j-i+1 ) {
                resLength = j-i+1;
                res_l = i;
                res_r = j;
            }
                
            i--;
            j++
        }
    }
};