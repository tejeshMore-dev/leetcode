/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let result = 0;
    let counter = 0;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            result = Math.max(counter, result);
            counter = 0;
        } else {
            counter++;
        }
    }
    
    result = Math.max(counter, result);
    return result;
};