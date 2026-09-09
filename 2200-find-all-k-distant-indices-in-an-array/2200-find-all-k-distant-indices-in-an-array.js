/**
 * @param {number[]} nums
 * @param {number} key
 * @param {number} k
 * @return {number[]}
 */
var findKDistantIndices = function(nums, key, k) {
    let arr = [];
    let ans = [];
    
    for( let i in nums ) {
        if( nums[i] === key ) {
            arr.push(i);        
        }
    }
    
    for( let i in nums ) {
       for( let j of arr ) {
           if( Math.abs( i-j ) <= k ) {
               ans.push(i)
               break;
           }
       }
    }
    
    return ans;
};