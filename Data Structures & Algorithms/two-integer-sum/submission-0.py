class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in track:
                return[track[need], i]
            track[nums[i]] = i


        