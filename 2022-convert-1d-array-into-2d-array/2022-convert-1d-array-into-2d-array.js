/**
 * @param {number[]} original
 * @param {number} m
 * @param {number} n
 * @return {number[][]}
 */
var construct2DArray = function(original, m, n) {
    if( original.length !== m*n ) return [];
    let result = [];
    
    for( let i=0; i<m; i++ ) {
        let row = [];
        
        for( let j=0; j<n; j++ )
            row.push( original[i * n + j] )
        
        result.push([...row]);
    }
    
    return result;
};