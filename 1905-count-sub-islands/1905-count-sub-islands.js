/**
 * @param {number[][]} grid1
 * @param {number[][]} grid2
 * @return {number}
 */
var countSubIslands = function(grid1, grid2) {
    let rows = grid2.length;
    let cols = grid2[0].length;
    let visited = new Set();
    let ans = 0;
    
    for( let r=0; r<rows; r++ ) {
        for( let c=0; c<cols; c++ ) {
            if( grid2[r][c] === 1 && !visited.has(`${r}-${c}`) && validate(r, c) )
                ans++;
        }
    }
    
    return ans;
    
    
    function validate(r, c) {
        if( r<0 || c<0 || r === rows || c === cols || visited.has(`${r}-${c}`) || grid2[r][c] == 0 )
            return true;
        
        visited.add(`${r}-${c}`);
        let res = true;
        
        if( grid1[r][c] === 0 )
            res = false;
        
        res = validate(r+1, c) && res;
        res = validate(r-1, c) && res;
        res = validate(r, c+1) && res;
        res = validate(r, c-1) && res;
    
        return res;
    }
};