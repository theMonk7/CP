class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res: list[list[str]] = []
        self.helper(s, res, [])
        return res

    def helper(self, s: str, res: list[list[str]], temp: list[str]) -> None:
        if s == "":
            res.append(temp)
            return

        for i in range(len(s)):
            s1 = s[:i + 1]
            if s1 != s1[::-1]:
                continue
            temp.append(s1)
            self.helper(s[i + 1:], res, temp[:])
            temp.pop()
