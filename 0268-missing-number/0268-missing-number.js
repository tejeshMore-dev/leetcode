/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let result;
    
    for ( let i=0; i<nums.length; i++ ) {
        result ^= ( (i+1) ^ nums[i] );
    }
    
    return result
};