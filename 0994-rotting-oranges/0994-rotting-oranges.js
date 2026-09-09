/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    let rows = grid.length, cols = grid[0].length;
    let directions = [ [1, 0], [-1, 0], [0, 1], [0, -1] ];
    let queue = [];
    let minM = 0;
    let freshO = 0;
    
    for( let r=0; r < rows; r++ ) {
        for( let c=0; c<cols; c++ ) {
            if( grid[r][c] === 2 ) {
                queue.push([r, c]);
            } else if( grid[r][c] === 0 )
                grid[r][c] = 2
            else
                freshO++;
        }
    }
    
    if( freshO === 0 )
        return 0;
    
    while( queue.length > 0 ) {
        let length = queue.length;
        
        for( let i=0; i < length; i++ ) {
            let [r, c] = queue.shift();
            
            directions.map((direction) => {
                let [ rD, cD ] = direction;
                let rN = rD+r, cN = cD+c;
                
                if( rN >= 0 && cN >= 0 && rN< rows && 
                   cN < cols && grid[rN][cN] === 1 ) {
                    queue.push([rN, cN]);
                    grid[rN][cN] = 2;
                    freshO--;
                }
            });
        }
        
        if(queue.length > 0) {
            minM++;
        }
    }
    
    return freshO == 0 ? minM : -1;
};