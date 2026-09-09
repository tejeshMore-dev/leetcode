/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    let cache = {};
    const MAX =Number.MAX_VALUE;
    
    let ans = findMinCoin(amount);
    return ans === MAX ? -1 : ans;
    
    function findMinCoin(amount) {
        if( cache[amount] )
            return cache[amount];
        
        if( amount === 0 )
            return 0
                
        let res = MAX;
        for( let coin of coins ) {
            if( coin <= amount )
                res = Math.min(res, 1 + findMinCoin(amount-coin));
        }
        
        cache[amount] = res;
        return res
    }
};

/*
551


*/