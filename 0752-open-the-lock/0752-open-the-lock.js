/**
 * @param {string[]} deadends
 * @param {string} target
 * @return {number}
 */
var openLock = function(deadends, target) {
    let visited = new Set( deadends );
    if( visited.has(target) ||  visited.has("0000") )
        return -1;
    
    let queue = [ [ [0, 0, 0, 0], 0 ] ] // start turns
    
    while( queue.length ) {
        let [ curr, turns ] = queue.shift();
        
        if( curr.join("") === target )
            return turns
        
        for( let opt of options(curr) ) {
            if( visited.has(opt.join("")) )
                continue;
            
            visited.add(opt.join(""));
            queue.push( [ opt, turns+1 ] );
        }
    }
    return -1;
    
    function options(curr) {
        let res = [];
        for( let i=0; i < curr.length; i++ ) {
            let curr1 = [ ...curr ];
            let temp = curr1[i];
            curr1[i] = (curr1[i] + 1)%10;
            res.push( [...curr1]);
            
            curr1[i] = temp;
            curr1[i] = (curr1[i] - 1+10)%10;
            res.push( [...curr1]);
        }
        return res;
    }
};