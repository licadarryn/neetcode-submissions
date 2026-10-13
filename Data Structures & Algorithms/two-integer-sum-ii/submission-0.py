class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        track = {}

        for i in range(len(numbers)):
            need = target - numbers[i]
            if numbers[i] in track:
                return [track[numbers[i]] + 1, i + 1]
            track[need] = i