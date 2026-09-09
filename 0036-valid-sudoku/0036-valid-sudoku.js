/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    let rows = board.length, cols = board[0].length;
    let rowMap = {};
    let colMap = {};
    let subBoxMap = {};

    for( let r=0; r<rows; r++ ) {
        for( let c=0; c<cols; c++ ) {
            let val = board[r][c];

            if( val === "." )
                continue;
            
            if(!rowMap[r])
                rowMap[r] = new Set();
            
            if(!colMap[c])
                colMap[c] = new Set();

            let key = `${Math.floor(r/3)}-${Math.floor(c/3)}`;
            if(!subBoxMap[key])
                subBoxMap[key] = new Set();

            if(rowMap[r].has(val) || colMap[c].has(val) || subBoxMap[key].has(val))
                return false

            
            rowMap[r].add(val);
            colMap[c].add(val);
            subBoxMap[key].add(val);
        }
    }

    return true
};