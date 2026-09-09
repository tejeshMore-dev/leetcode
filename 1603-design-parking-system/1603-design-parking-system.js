/**
 * @param {number} big
 * @param {number} medium
 * @param {number} small
 */
let parkingSpaceMap = {}
let carTypes = {
    big: '1',
    medium: '2',
    small: '3'
}

var ParkingSystem = function(big, medium, small) {
    parkingSpaceMap = {
        [carTypes.big]: big,
        [carTypes.medium]: medium,
        [carTypes.small]: small
    }
};

/** 
 * @param {number} carType
 * @return {boolean}
 */
ParkingSystem.prototype.addCar = function(carType) {
    if(!parkingSpaceMap[carType] || parkingSpaceMap[carType] < 1)
    return false
    
    parkingSpaceMap[carType] = parkingSpaceMap[carType] - 1;
    return true
};

/** 
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = new ParkingSystem(big, medium, small)
 * var param_1 = obj.addCar(carType)
 */