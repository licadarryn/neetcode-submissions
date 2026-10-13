class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}
        for num in nums:
            if num not in track:
                track[num] = 0
            track[num] += 1

        track =dict(sorted(track.items(), key = lambda kv:kv[1], reverse = True))

        return list(track.keys())[:k]
        