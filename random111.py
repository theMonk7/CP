def max_word(s: str, banned):
    hm = {}
    t = s.split(" ")
    ans = ""
    ans_cnt = 0
    for element in t:
        if element not in banned:
            if hm.__contains__(element):
                hm[element] += 1

            else:
                hm[element] = 1
            if ans_cnt < hm[element]:
                ans_cnt = hm[element]
                ans = element

    return ans
