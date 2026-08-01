class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum_product = nums[0]
        minimum_product = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):

            previous_maximum = maximum_product
            previous_minimum = minimum_product

            maximum_product = max(nums[i],
                                    nums[i] * previous_maximum,
                                    nums[i] * previous_minimum)

            minimum_product = min(nums[i],
                                    nums[i] * previous_maximum,
                                    nums[i] * previous_minimum)
            
            ans = max(ans, maximum_product)
        
        return ans

