/**
 * @param {number} n
 * @param {number} target
 * @return {number}
 */
var makeIntegerBeautiful = function(n, target) {
    let num = [];
    
    while( n ) {
        num.push(n%10);
        n = Math.floor(n/10);
    }
    
    let ans = []
    for( let i=0; i<num.length; i++ ) {
        let n = num[i];
        
        if( findSum() > target ) {
            let diff = 10 - n
            ans.push(diff);
            num[i] = 0;
            
            if( i+1 >= 0 )
                num[i+1] = num[i+1] + 1
        }
    }
    return ans.reduce((sum, val, i) => sum+(val* (Math.pow(10, i))), 0);
    
    function findSum() {
        return num.reduce((sum, val) => sum+val, 0);
    }
};