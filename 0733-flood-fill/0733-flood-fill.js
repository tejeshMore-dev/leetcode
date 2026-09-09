/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, newColor) {
    const ROWS = image.length, COLS = image[0].length;
    let visited = new Set();
    let startingPixel = image[sr][sc];
    let directions = [[-1, 0], [0, -1], [1, 0], [0, 1]];
    
    dfs( [ [sr, sc] ]);
    return image;
    
    function dfs( queue ) {
        while( queue.length ) {
            let [ r, c ] = queue.pop();
            image[r][c] = newColor;
            
            for( let direction of directions ) {
                let [ rD, cD ] = direction;
                rD += r;
                cD += c;
                
                if( rD >= 0 && cD >= 0 && rD < ROWS && cD < COLS && image[rD][cD] === startingPixel && !visited.has(`${rD}-${cD}`) ) {
                    queue.push([rD, cD]);
                    visited.add(`${rD}-${cD}`);
                }
            }
        }
    }
};