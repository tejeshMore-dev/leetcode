/**
 * @param {string} s
 * @return {number}
 */

//longestPalindromeSubseq
var longestPalindromeSubseq = function(s) {
  var sols = new Array(s.length).fill(0).map(a => new Array(s.length).fill(-1));
    return helper( s, 0, s.length-1, sols );
};

function helper( s, l, r, sols ) {
    if( l === r )
        return 1
    
    if( l > r )
        return 0
    
    if (sols[l][r] !== -1) return sols[l][r];
    
    if( s.charAt(l) === s.charAt(r) ) {
       return sols[l][r] = 2 + helper( s, l+1, r-1, sols );
    } else {
        return sols[l][r]  = Math.max( helper(s, l, r-1, sols), helper(s, l+1, r, sols) );
    }
}

// longestCommonSubsequence
// var longestCommonSubsequence = function(text1, text2) {
//   var sols = new Array(text1.length).fill(0).map(a => new Array(text2.length).fill(-1));
//     return helper( text1, text2, text1.length-1, text2.length-1, sols )
// };

// function helper( text1, text2, n, m, sols ) {
//     if( n < 0 || m < 0 )
//         return 0;

//     if (sols[n][m] !== -1) return sols[n][m];


//     if( text1.charAt(n) === text2.charAt(m) ){
//         return sols[n][m] = 1 + helper( text1, text2, n-1, m-1, sols );            
//     } else {
//         return sols[n][m] = Math.max( helper( text1, text2, n, m-1, sols ), 
//                                              helper( text1, text2, n-1, m, sols ) );
//     }
// }