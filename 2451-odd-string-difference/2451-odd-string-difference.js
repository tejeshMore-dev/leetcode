/**
 * @param {string[]} words
 * @return {string}
 */
var oddString = function(words) {
    let map = {};
    
    for( let word of words ){
        let diffStr = findDiffStr(word);
        // console.log(word, diffStr)
        if( !map[diffStr] )
            map[diffStr] = [];

        map[diffStr].push(word);
    }

    // console.log(map)
    for( let key in map ) {
        if( map.hasOwnProperty(key) && map[key].length === 1 )
            return map[key][0]
    }

    function findDiffStr(str) {
        let sb = [];

        for( let i=0; i<str.length-1; i++ ) {
            let diff = (str.charCodeAt(i+1) - 'a'.charCodeAt(0)) - (str.charCodeAt(i) - 'a'.charCodeAt(0)) 
            // console.log(diff);
            sb.push(+diff, "_")
        }

        return sb.join("");
    }
};