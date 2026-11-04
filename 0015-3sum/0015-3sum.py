class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        N = len(nums)
        ans = []

        for i in range(N - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, N - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                if current_sum < 0:
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                else:
                    right -= 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return ans
