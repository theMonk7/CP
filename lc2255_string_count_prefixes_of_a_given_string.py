class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        cnt = 0
        for word in words:
            if word == s[:len(word)]:
                cnt += 1

        return cnt