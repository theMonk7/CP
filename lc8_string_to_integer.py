class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        plus = dig = -1
        sign = False
        for i in range(len(s)):
            if dig != -1:
                break
            if s[i] == " ":
                continue
            elif s[i] == "+" or s[i] == "-":
                if plus == -1:
                    plus = i
                    sign = True if s[i] == "-" else False
                else:
                    return 0
            elif s[i].isalpha() or (s[i].isascii() and not s[i].isalnum()):
                if dig == -1:
                    return 0
                else:
                    break
            elif s[i].isdigit():
                dig = i
                ans = 10 * ans + int(s[i])

        ans = ans if not sign else -1 * ans
        if ans < -2 ** 31:
            return -2 ** 31
        elif ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return ans

#         ans = 0
#         minus = False
#         started = False
#         for i in range(len(s)):
#             if e == " " or e == "+" or e == "-":
#                 continue
#             elif e.isalpha() or (e.isascii() and not e.isalnum()) or ((e == "+" or e == "-") and ):
#                 return 0
#             elif e.isdigit():
#                 break
#         for i in range(len(s)):
#             if s[i].isdigit():
#                 started = True
#                 ans = 10*ans + int(s[i])
#             elif s[i] == "-" and i < len(s)-1 and s[i+1].isdigit():
#                 minus = True
#             else:
#                 if started:
#                     break
#         ans = ans if not minus else -1*ans
#         if ans < -2**31:
#             return -2**31
#         elif ans > 2**31-1:
#             return 2**31-1
#         else:
#             return ans

print(Solution().myAtoi("00000-42a1234"))