class Solution:
    def isValid(self, s: str) -> bool:
        check = {"}": "{", ")": "(", "]": "["}
        track_s = []

        for c in s:
            if c not in check:
                track_s.append(c)
            else:
                if not track_s:
                    return False
                curr = track_s.pop()
                if curr != check[c]:
                    return False

        return len(track_s) == 0