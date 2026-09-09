/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    let result = 0;
    
    for (let i=0; i<nums.length; i++) {
       if ( Math.floor(Math.log10(nums[i])) % 2 !== 0 )
           result++;
    }
    
    return result;
};