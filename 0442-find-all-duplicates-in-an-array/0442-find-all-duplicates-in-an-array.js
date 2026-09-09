/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    let result = [];
    
    for( let i=0; i<nums.length; i++ ) {
        let index = Math.abs(nums[i]) - 1;
        if( nums[index] < 0 ) result.push(Math.abs(nums[i]))
        
        nums[ index ] *= -1;
    }
    
    return result;
};