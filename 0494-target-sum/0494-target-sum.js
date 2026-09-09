/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var findTargetSumWays = function(nums, target) {
    let cache = new Map();
    return findWays(0, 0);
    
    function findWays(i, sum) {
        let cacheKey =  `${i}-${sum}`;
        if( cache.has(cacheKey) )
            return cache.get(cacheKey);
        
        if(  i === nums.length && sum === target )
            return 1
        
        if( i >= nums.length )
            return 0
        
        let res = 0;
        res += findWays(i+1, sum + nums[i]);
        res += findWays(i+1, sum - nums[i]);
        
        cache.set(cacheKey,res);
        return res;
    }
};