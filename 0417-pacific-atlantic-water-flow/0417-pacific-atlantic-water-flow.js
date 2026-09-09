/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function(heights) {
    const ROWS = heights.length;
    const COLS = heights[0].length;
    
    let pSet = new Set();
    let aSet = new Set();
    
    for( let r=0; r < ROWS; r++ ) {
        dfs( r, 0, heights[r][0], pSet );
        dfs( r, COLS-1, heights[r][COLS-1], aSet );
    }
    
    for( let c=0; c < COLS; c++ ) {
        dfs( 0, c, heights[0][c], pSet );
        dfs( ROWS-1, c, heights[ROWS-1][c], aSet );
    }
    
    let result = [];
    for( let r=0; r<ROWS; r++ ) {
        for( let c=0; c<COLS; c++ ) {
            if( pSet.has(`${r}-${c}`) && aSet.has(`${r}-${c}`) )
                result.push([r, c]);
        }
    }
    
    return result;
    
    
    function dfs( r, c, prev, set ) {
        if( r < 0 || c < 0 || r >= ROWS || c >= COLS || set.has(`${r}-${c}`) || heights[r][c] < prev  )
            return;
        
        set.add(`${r}-${c}`);
        dfs(r+1, c, heights[r][c], set);
        dfs(r-1, c, heights[r][c], set);
        dfs(r, c+1, heights[r][c], set);
        dfs(r, c-1, heights[r][c], set);
    }
};