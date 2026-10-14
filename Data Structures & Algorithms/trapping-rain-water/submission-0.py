class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l = 0
        r = n - 1

        left_max = float('-inf')
        right_max = float('-inf')
        total = 0

        while l < r:
            if  height[l] <= height[r]:
                left_max = max(left_max, height[l])
                total += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                total += right_max - height [r]
                r -= 1

        return total