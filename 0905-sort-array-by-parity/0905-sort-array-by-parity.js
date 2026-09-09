/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
    let lp = 0;
    let hp = nums.length-1;
    
    while (lp<hp) {
        let lEven = nums[lp] % 2 === 0;
        let hOdd = nums[hp] % 2 !== 0;
        
        if(lEven && hOdd){
            lp++;
            hp--
        } else if(!lEven && !hOdd){
            let temp = nums[lp];
            nums[lp] = nums[hp];
            nums[hp] = temp
        } else if(lEven && !hOdd){
            lp++;
        } else if(!lEven && hOdd){
            hp--;
        }
    }
    return nums
};