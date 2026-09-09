/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if(prices.length === 1 )
        return 0

    let lp = prices[0], maxP = 0;

    for( let i=1; i < prices.length; i++ ) {
        let profit = prices[i] - lp;

        lp = Math.min(lp, prices[i]);
        maxP = Math.max(maxP, profit);
    }

    return maxP
};