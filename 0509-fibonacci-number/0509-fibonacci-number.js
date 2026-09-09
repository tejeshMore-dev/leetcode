/**
 * @param {number} n
 * @return {number}
 */

let cache = {};
var fib = function(n) {
    if(cache[n]) {
       return cache[n]
    }
    
    let result;
    if(n < 2 ) {
        result = n
    } else {
        result = fib(n-1) + fib(n-2)
    }
    
    cache[n] = result;
    return result
};