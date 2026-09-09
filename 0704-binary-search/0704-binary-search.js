/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    if ( nums.length === 0 )
        return -1
    
    if( nums.length === 1 && nums[0] === target )
        return 0

    let lp=0, rp=nums.length-1, mid;
    let result= -1;

    while( lp <= rp ) {
        mid = Math.floor((rp+lp)/2);

        if( nums[mid] === target ) {
            result = mid;
            break
        } else if ( nums[mid] > target ) {
            rp = mid-1
        } else {
            lp = mid+1;
        }
    }

    return result;
};