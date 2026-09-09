/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumDifference = function(nums, k) {
    if( nums.length < 2 )
        return 0;
    
    nums.sort((a,b) => a-b);
    let l=0, r= k-1;
    let res = Number.MAX_VALUE;
    
    while( r < nums.length ) {
        let diff = nums[r] - nums[l];
        res = Math.min(diff, res);
        r++;
        l++;
    }
    
    return res;
};
/*
res
sort inc

k size window
diff = num[r] - nums[l]
res = Mth.min








*/