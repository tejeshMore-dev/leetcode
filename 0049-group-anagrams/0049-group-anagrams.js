/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let map = {};

    for( let str of strs ) {
        let pattern = getAnagramPattern(str)

        if( !map[pattern] )
            map[pattern] = [];

        map[pattern].push(str);
    }

    let res = [];
    for( let key in map ) {
        res.push(map[key]);
    }
    return res;

    function getAnagramPattern(str) {
        let arr = new Array(26).fill(0);

        for( let char of str ) {
            let diff = char.charCodeAt(0) - 'a'.charCodeAt(0);

            arr[diff] = arr[diff] + 1; 
        }

        return arr.join("-");
    }
};