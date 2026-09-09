
var TwoSum = function() {
    this.map = new Map();
};

/** 
 * @param {number} number
 * @return {void}
 */
TwoSum.prototype.add = function(number) {
    this.map.set (number, this.map.has(number) ? this.map.get(number) + 1 : 1);
};

/** 
 * @param {number} value
 * @return {boolean}
 */
TwoSum.prototype.find = function(value) {
    for( let key of this.map.keys() ) {
        let num1 = parseInt(key);
        let num2  = value - num1;
        
        if( num1 === num2 && this.map.get(num1) > 1 )
            return true
        else if(  num1 !== num2 && this.map.has(num2) )
            return true           
    }
    
    return false;
};

/** 
 * Your TwoSum object will be instantiated and called as such:
 * var obj = new TwoSum()
 * obj.add(number)
 * var param_2 = obj.find(value)
 */