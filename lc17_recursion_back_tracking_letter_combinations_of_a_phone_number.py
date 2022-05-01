class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []
        self.hash_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        # self.solver(digits, 0, result, [])
        self.solver_2(digits, result, [])
        return result

    def solver(self, num_str: str, num_str_index: int, result: list[str], temp: list[str]):
        if len(temp) == len(num_str):
            result.append("".join(temp))
            return

        for i in range(num_str_index, len(num_str)):
            c_set = self.hash_map[num_str[i]]

            for j in range(len(c_set)):
                # temp.append(c_set[j])
                self.solver(num_str, i + 1, result, temp + [c_set[j]])
                # temp.pop()

    def solver_2(self, num_str: str, result: list[str], temp: list[str]):
        if len(num_str) == 0:
            result.append("".join(temp))
            return
        c_set = self.hash_map[num_str[0]]
        for j in range(len(c_set)):
            # temp.append(c_set[j])
            self.solver_2(num_str[1:], result, temp + [c_set[j]])
            # temp.pop()


print(Solution().letterCombinations("23"))
