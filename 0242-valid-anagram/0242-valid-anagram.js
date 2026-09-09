/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if( s.length !== t.length )
        return false

    let sMap = new Map();
    let tMap = new Map();

    for( let char of s ) {
        if( sMap.has(char) )
            sMap.set(char, sMap.get(char)+1)
        else 
            sMap.set(char, 1)     
    }

    for( let char of t ) {
        if( tMap.has(char) )
            tMap.set(char, tMap.get(char)+1)
        else 
            tMap.set(char, 1)     
    }

    for( let val of tMap ) {
       let [char, tFrequency ] = val;

       if( sMap.get(char) !== tFrequency )
        return false
    }

    return true
};