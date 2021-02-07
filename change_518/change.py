"""
518. 零钱兑换 II

给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。



示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。

示例 3:

输入: amount = 10, coins = [10]
输出: 1



注意:

你可以假设：

    0 <= amount (总金额) <= 5000
    1 <= coin (硬币面额) <= 5000
    硬币种类不超过 500 种
    结果符合 32 位符号整数
"""
from typing import List


def change(amount: int, coins: List[int]) -> int:
    # TODO
    coins.sort()
    dp = [0] * (amount + 1)
    for i in range(0, len(dp)):
        if i == 0:
            dp[i] = 0
            continue
        if i in set(coins):
            dp[i] = 1
        visited = set()
        for j in range(0, len(coins)):
            if i - coins[j] <= 0:
                break
            if i - coins[j] > 0 and (i - coins[j]) not in visited:
                dp[i] += dp[i - coins[j]]
            if i - coins[j] in set(coins):
                visited.update({i - coins[j], coins[j]})
    return dp[-1]


if __name__ == "__main__":
    print(change(4, [1, 2, 5]))
