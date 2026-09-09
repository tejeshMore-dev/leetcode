/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let set = new Set(); //memory

    for(let num of nums ) {
        if( set.has(num) ) //already know in momory
            return true
        
        set.add(num); //add in memory
    }

    return false;

    /*
    // TC: O(n2)
    // SC: O(1)

    for( let i=0; i<nums.length; i++ ){
        for( let j=0; j<nums.length; j++ ) {
            if( i !== j ) {
                if( nums[j] === nums[i] ){
                    return true
                }
            }
        }
    }

    return false
    */
};
/*
[1,2,3,1]




memory:{ }










*/