/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let prefixProduct = new Array(nums.length+1).fill(1);
    let suffixProduct = new Array(nums.length+1).fill(1);
    
    for( let i=1; i<nums.length; i++ ) {
        prefixProduct[i] = nums[i-1] * prefixProduct[i-1]
    }

    for( let i=nums.length-1; i>=0; i-- ) {
        suffixProduct[i] = nums[i] * suffixProduct[i+1];
    }
    
    let res = [];
    console.log(prefixProduct, suffixProduct)
    for( let i=0; i<nums.length; i++ ) {
        res.push(prefixProduct[i] * suffixProduct[i+1])
    }
    return res;
};

/*
       1  2  3  4
    1  1  2  6  24
       24 24 12  4   1 
*/