class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        ans = float('-inf')

        while i < j:
            width = j - i
            height = min(heights[i], heights[j])
            curr = width * height

            ans = max(curr, ans)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return ans