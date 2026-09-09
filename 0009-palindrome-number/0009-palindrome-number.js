/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0)
        return false
    
    let input = x.toString();
    let lp = 0;
    let hp = input.length - 1;

    while (hp > lp) {
        if(input[hp] !== input[lp])
            return false;
        
        lp++;
        hp--;
    }
    return true;
};