/**
 * @param {number[]} matchsticks
 * @return {boolean}
 */
var makesquare = function(matchsticks) {
    let total = 0;
    const SIDES = 4;
    for( let l of matchsticks ) {
        total += l;
    }
    if( total%SIDES )
        return false;
    
    let target = total/SIDES;
    let used = new Array(matchsticks.length).fill(false);
    return backtrack( i=0, SIDES, currSum=0 );
    
    function backtrack( i, sides, currSum ) {
        if( sides === 0 )
            return true
        
        if( currSum === target )
            return backtrack( 0, sides-1, 0 )
        
        for( let j=i; j < matchsticks.length; j++ ) {
            if( used[j] || currSum + matchsticks[j] > target )
                continue
            
            used[j] = true;
            if( backtrack( j+1, sides, currSum + matchsticks[j] ) )
                return true;
            used[j] = false;
        }
        
        return false;
    }
};