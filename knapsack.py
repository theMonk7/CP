def unboundedKnapsack(n, w, profit, weight):
    dp = [[0] * (w + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            not_take = dp[i - 1][j]
            take = -1000000000000000000
            if weight[i - 1] <= j:
                take = dp[i][j - weight[i - 1]] + profit[i - 1]
            dp[i][j] = max(take, not_take)
    print_selected_items_ub(dp, weight, w)
    return dp[n][w]


def boundedKnapsack(n, w, profit, weight):
    dp = [[0] * (w + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            not_take = dp[i - 1][j]
            take = -1000000000000000000
            if weight[i - 1] <= j:
                take = dp[i - 1][j - weight[i - 1]] + profit[i - 1]
            dp[i][j] = max(take, not_take)
    print_selected_items_b(dp, weight, w)

    return dp[n][w]


def print_selected_items_b(dp, weights, capacity):
    idxes_list = []
    print("Selected weights are: ", end='')
    n = len(weights)
    i = n

    while i >= 0 and capacity >= 0:
        if i > 0 and dp[i][capacity] != dp[i - 1][capacity]:
            idxes_list.append(i)
            capacity -= weights[i - 1]
        i -= 1
    weights = [weights[idx - 1] for idx in idxes_list]
    print(weights)
    return weights


def print_selected_items_ub(dp, weights, capacity):
    idxes_list = []
    print("Selected weights are: ", end='')
    n = len(weights)
    i = n
    while i >= 0 and capacity >= 0:
        if i > 0 and dp[i][capacity] != dp[i - 1][capacity]:
            # include this item
            idxes_list.append(i - 1)
            capacity -= weights[i - 1]
        # elif i == 0 and capacity >= weights[i-1]:
        #     # include this item
        #     idxes_list.append(i)
        #     capacity -= weights[i-1]
        else:
            i -= 1
    print(idxes_list)
    weights = [weights[idx] for idx in idxes_list]
    print(weights)
    return weights


n = 6
w = 7
profit = [1, 4, 8, 6, 9, 4]
weight = [1, 2, 4, 5, 7, 8]


# print(unboundedKnapsack(n, w, profit, weight))
# print(boundedKnapsack(n, w, profit, weight))
def mySqrt(x: int) -> int:
    l = 0
    r = x
    while l < r:
        m = (l + r) // 2
        if m * m > x:
            r = m
        else:
            l = m + 1
    return l - 1


print(mySqrt(15))
