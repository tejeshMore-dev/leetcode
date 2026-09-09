/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    if(!x)
        return 0
    
    let isNegative = x < 0;
    let result = 0;
    
    isNegative && ( x = x*-1 )
    
    while (x > 0) {
        let reminder = x%10;
        x = Math.floor(x/10);
        
        result = result * 10 + reminder;
        
        if( result > Math.pow(2,31) )
         return result = 0;
    }
    
    isNegative && ( result = result*-1 )
    return result      
};