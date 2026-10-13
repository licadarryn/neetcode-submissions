class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = sorted(set(nums))

        ans = 1
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                curr += 1
            else:
                ans = max(ans, curr)
                curr = 1

        return  max(ans, curr)       