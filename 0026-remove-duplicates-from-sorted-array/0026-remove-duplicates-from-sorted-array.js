/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if( nums.length < 2 )
        return nums.length;
    
    let i = 1, ri = 1;
    
    while( i < nums.length ) {
        if( nums[i] !== nums[i-1] ) {
            nums[ri] = nums[i];
            ri++;
        }
        
        i++;
    }
    
    return ri;
};
