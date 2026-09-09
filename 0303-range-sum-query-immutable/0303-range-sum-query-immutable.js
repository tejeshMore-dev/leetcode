/**
 * @param {number[]} nums
 */

var NumArray = function(nums) {
    let prev = 0;
    this.prefixSum = new Array(nums);
    
    for(let i=0; i<nums.length; i++) {
        this.prefixSum[i] = prev + nums[i];
        prev = this.prefixSum[i]
    }   
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {number}
 */
NumArray.prototype.sumRange = function(left, right) {
    if(left === 0)
        return this.prefixSum[right]
    
    return this.prefixSum[right] - this.prefixSum[left - 1]
};

/** 
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */