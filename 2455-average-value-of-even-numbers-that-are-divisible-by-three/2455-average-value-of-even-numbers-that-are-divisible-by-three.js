/**
 * @param {number[]} nums
 * @return {number}
 */
var averageValue = function(nums) {
    let res = 0, length=0
    
    for( let num of nums ) {
        if( num%2 === 0 && num%3 === 0 ) {
            res += num;
            length++;
        }    
    }
    
    return res ? Math.floor(res/length) : 0
};