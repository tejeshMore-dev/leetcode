class Solution:

    @staticmethod
    def rotate_arr(arr: list, l: int, r: int) ->None:
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l

        self.rotate_arr(nums, 0,  l - 1)
        self.rotate_arr(nums, 0,  k - 1)
        self.rotate_arr(nums, k,  l - 1)



