class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        total_units = 0
        total_boxes = 0

        for boxes, units in boxTypes:
                allowed = min(truckSize - total_boxes, boxes)
                total_units += allowed * units
                total_boxes += allowed

        return total_units


        